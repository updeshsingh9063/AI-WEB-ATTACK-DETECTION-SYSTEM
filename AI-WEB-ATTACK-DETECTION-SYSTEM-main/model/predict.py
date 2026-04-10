import joblib

model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

def predict(text):
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    return pred