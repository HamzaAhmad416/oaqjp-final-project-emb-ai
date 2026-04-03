import requests

def emotion_detector(text_to_analyse):

    url = "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_multi_stock"
    }

    response = requests.post(url, json=payload, headers=headers)

    # ❌ handle bad request
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    result = response.json()

    # ❌ SAFE CHECK (IMPORTANT FIX)
    if "emotionPredictions" not in result:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    emotions = result["emotionPredictions"][0]["emotion"]

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }