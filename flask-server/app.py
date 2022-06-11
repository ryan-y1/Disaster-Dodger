from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Bonjour Tout Le Monde"

if __name__ == "__main__":
    app.run(debug=True)