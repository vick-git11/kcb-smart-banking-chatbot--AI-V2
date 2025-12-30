from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.timezone import localtime

from .ai.intent_model import predict_intent
from .ai.risk_model import predict_risk
from .ai.router import route
from .ai.faq_engine import search_faq
from .ai.tools import run_tool
from .models import ChatLog

@api_view(["POST"])
def chat(request):
    text = request.data.get("message", "")
    authenticated = request.data.get("authenticated", False)

    intent = predict_intent(text)
    risk = predict_risk(text)
    destination = route(intent, risk, authenticated)

    confidence = None
    tool_data = None

    # Live API + Semantic FAQ
    if destination in ["FAQ", "GUIDE"]:
        tool_data = run_tool(intent, text)

        if tool_data:
            # Provide a specialized message for branches
            if isinstance(tool_data, list) and len(tool_data) > 0 and "latitude" in tool_data[0]:
                reply = "Here are nearby branches I found:"
            elif isinstance(tool_data, dict) and "error" in tool_data:
                reply = f"Live branch lookup failed: {tool_data['error']}"
            else:
                reply = f"Here is the latest information I found: {tool_data}"
        else:
            answer, confidence = search_faq(text)

            if answer is None:
                reply = (
                    "I want to make sure you get accurate and secure information. "
                    "I’m not fully confident I have the right answer. "
                    "Let me connect you to the right support team."
                )
            else:
                if destination == "FAQ":
                    reply = answer
                else:
                    reply = f"{answer} If you would like, I can guide you through the steps."
    elif destination == "SECURE_APP":
        reply = (
            "For your security, this request must be handled inside the secure "
            "mobile banking app."
        )
    else:
        reply = (
            "This request involves sensitive banking information. "
            "Please log in to continue."
        )

    log = ChatLog.objects.create(
        user_message=text,
        intent=intent,
        risk=risk,
        route=destination,
        reply=reply,
        confidence=confidence
    )

    return Response({
        "reply": reply,
        "intent": intent,
        "risk": risk,
        "route": destination,
        "confidence": confidence,
        "created_at": localtime(log.created_at).isoformat(),
        "live_data": tool_data
    })
