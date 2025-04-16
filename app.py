from flask import Flask, render_template, request
import scanner
import database
import web_scanner

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    target = request.form["target"]
    scan_results = scanner.scan_ports(target)
    database.save_scan_results(target, scan_results)
    return render_template("results.html", results=scan_results)

@app.route("/history")
def history():
    results = database.get_scan_results()
    return render_template("results.html", results=results)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form["url"]
        result = web_scanner.check_xss(url)
    return render_template("index.html", result=result)


if __name__=="__main__":
    app.run(debug=True)
