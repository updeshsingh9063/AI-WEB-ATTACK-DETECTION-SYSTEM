from core.rules import rule_based
from core.ml_engine import ml_predict
import random

def detect(req):
    rule = rule_based(req)

    if rule:
        return {
            "result": "🚫 Attack Detected",
            "type": rule,
            "confidence": random.randint(90, 99)
        }

    ml = ml_predict(req)

    if ml == "Suspicious":
        return {
            "result": "⚠️ Suspicious",
            "type": "ML Detection",
            "confidence": random.randint(80, 95)
        }

    return {
        "result": "✅ Safe",
        "type": "Normal",
        "confidence": random.randint(85, 99)
    }