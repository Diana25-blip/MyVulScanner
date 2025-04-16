import requests

def check_sql_injection(url):
    payload = "' OR '1'='1"
    res = requests.get(url + payload)

    if "SQL" in res.text or "syntax" in res.text:
        return f"Potential SQL Injection found at {url}"
    return "No SQLi detected."

def check_xss(url):
    payload = "<script>alert('XSS')</script>"
    res = requests.get(url + payload)

    if payload in res.text:
        return f"Potential XSS found at {url}"
    return "No XSS detected."
