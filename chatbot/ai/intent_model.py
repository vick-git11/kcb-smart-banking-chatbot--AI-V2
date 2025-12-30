
from transformers import pipeline

intent_classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased",
    top_k=1
)

def predict_intent(text):
    return intent_classifier(text)[0]
