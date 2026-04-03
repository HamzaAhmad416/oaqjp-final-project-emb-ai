from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

# ✅ Route to load frontend (IMPORTANT for web deployment)
@app.route("/")
def home():
    return render_template("index.html")

# ✅ Required API route
@app.route("/emotionDetector", methods=["GET"])
def emotionDetector():

    text_to_analyse = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyse)

    # ✅ Task 7 (error handling)
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    # ✅ REQUIRED FORMAT (strict)
    response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)