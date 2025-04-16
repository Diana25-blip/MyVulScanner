from flask import Flask, render_template, request
import scanner
import database
import requests

app = Flask(__name__)

def check_xss(url):
    payload = "<script>alert('XSS')</script>"
    try:
        res = requests.get(url + payload, timeout=5)

        if payload in res.text:
            return f"⚠️ Potential XSS found at: {url}"
        else:
            return "✅ No XSS detected."
    except requests.exceptions.RequestException as e:
        return f"❌ Error scanning URL: {e}"

#Home page
@app.route("/")
def index():
    return render_template("index.html")

#Scan port
@app.route("/scan", methods=["POST"])
def scan():
    target = request.form["target"]
    scan_results = scanner.scan_ports(target)
    database.save_scan_results(target, scan_results)
    return render_template("results.html", results=scan_results)

#scan History
@app.route("/history")
def history():
    results = database.get_scan_results()
    return render_template("results.html", results=results)

#XSS scanner route
@app.route("/xss", methods=["GET", "POST"])
def xss_scan():
    result = None
    if request.method == "POST":
        url = request.form["url"]
        result = check_xss(url)
    return render_template("xss.html", result=result)


if __name__=="__main__":
    app.run(debug=True)
