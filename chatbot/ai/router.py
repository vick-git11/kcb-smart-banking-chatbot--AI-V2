
def route(intent, risk, authenticated):
    if risk == "LOW":
        return "FAQ"

    if risk == "MEDIUM":
        return "GUIDE"

    if risk == "HIGH":
        if authenticated:
            return "SECURE_APP"
        else:
            return "LOGIN_REQUIRED"
