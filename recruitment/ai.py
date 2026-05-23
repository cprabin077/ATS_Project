from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_ats_score(job_text, resume_text):
    docs = [job_text, resume_text]
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(docs)
    similarity = cosine_similarity(matrix[0:1], matrix[1:2])
    return round(similarity[0][0] * 100, 2)

def get_recommendation(score):
    if score >= 80:
        return 'Final Interview'
    elif score >= 60:
        return 'Technical Interview'
    elif score >= 40:
        return 'HR Interview'
    return 'Rejected'