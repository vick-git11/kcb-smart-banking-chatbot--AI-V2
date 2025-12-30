from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

MODEL_NAME = "ProsusAI/finbert"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

# Map FinBERT sentiment to banking risk
RISK_MAP = {
    "positive": "LOW",     # neutral info, fees, hours
    "neutral": "MEDIUM",   # guidance, how-to, eligibility
    "negative": "HIGH"    # complaints, access, security, money
}

def predict_risk(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    
    with torch.no_grad():
        outputs = model(**inputs)

    probs = F.softmax(outputs.logits, dim=1)[0]
    label_id = torch.argmax(probs).item()
    label = model.config.id2label[label_id].lower()

    return RISK_MAP[label]
