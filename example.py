from flask import Flask, render_template
from main import generate_css

app = Flask(__name__)

with open("templates/index.html") as f:
    html = f.read()

@app.route("/")
def home():
    return render_template("index.html", css=generate_css(html))

app.run(host='0.0.0.0', port=81)