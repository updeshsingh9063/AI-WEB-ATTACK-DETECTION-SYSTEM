def rule_based(req):
    patterns = {
        "SQL Injection": ["OR 1=1", "UNION", "SELECT", "--"],
        "XSS": ["<script>", "alert(", "onerror"],
        "Path Traversal": ["../", "..\\"],
        "Command Injection": ["wget", "curl", "bash", "nc"]
    }

    for attack, keys in patterns.items():
        for k in keys:
            if k.lower() in req.lower():
                return attack

    return None