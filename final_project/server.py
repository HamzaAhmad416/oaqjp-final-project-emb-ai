from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def emotion_analysis():
    data = request.json
    text = data.get("text", "")

    result = emotion_detector(text)

    # ✅ TASK 7B: Handle invalid / blank input case
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # normal response
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)