from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from chatbot.models import FAQ

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_all_faqs():
    questions = []
    answers = []

    # 1. Load from Django Admin (DB)
    for f in FAQ.objects.all():
        questions.append(f.question)
        answers.append(f.answer)

    # 2. Load from CSV backup
    try:
        csv = pd.read_csv("chatbot/data/faqs.csv")
        for _, row in csv.iterrows():
            questions.append(str(row["question"]))
            answers.append(str(row["answer"]))
    except:
        pass

    if not questions:
        return [], [], []

    vectors = model.encode(questions)
    return questions, answers, vectors


def search_faq(query, threshold=0.50):
    questions, answers, vectors = load_all_faqs()

    if not questions:
        return None, 0.0

    query_vec = model.encode([query])
    scores = cosine_similarity(query_vec, vectors)[0]

    best_idx = int(np.argmax(scores))
    confidence = float(scores[best_idx])

    if confidence < threshold:
        return None, confidence

    return answers[best_idx], confidence
