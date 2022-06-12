from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/searchRegion", methods=['POST'])
def searchRegion():
    return jsonify("Ahhhh")


if __name__ == "__main__":
    app.run(debug=True)