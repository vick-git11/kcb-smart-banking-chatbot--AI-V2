
import pandas as pd
from risk_model import predict_risk

data = pd.read_csv("chatbot/data/training_data.csv")

correct = 0
for i,row in data.iterrows():
    if predict_risk(row["text"]) == row["risk"]:
        correct += 1

accuracy = correct / len(data)
print("Risk Model Accuracy:", accuracy)
