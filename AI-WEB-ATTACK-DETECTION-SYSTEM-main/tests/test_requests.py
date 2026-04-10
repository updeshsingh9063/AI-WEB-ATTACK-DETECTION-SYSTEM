from core.detector import detect

tests = [
    "GET /home",
    "admin' OR 1=1--",
    "<script>alert(1)</script>"
]

for t in tests:
    print(t, "->", detect(t))