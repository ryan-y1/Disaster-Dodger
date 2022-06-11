from crypt import methods
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Bonjour Tout Le Monde"

@app.route("/searchRegion", methods={"Post"})
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'


if __name__ == "__main__":
    app.run(debug=True)