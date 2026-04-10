import joblib

model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

def ml_predict(req):
    vec = vectorizer.transform([req])
    pred = model.predict(vec)[0]

    if pred == 1:
        return "Suspicious"
    return "Safe"