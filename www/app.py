from flask import Flask, request, render_template
from util import get_prediction_from_url

app = Flask(__name__)

@app.post("/check")
def check():
    body = request.get_json()
    if body is None or "url" not in body:
        return {"error": "URL is required."}, 400
    label = get_prediction_from_url(body["url"])
    return {"label": label}, 200

@app.route("/")
def index():
    return render_template("index.html")
