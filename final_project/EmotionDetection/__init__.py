import requests
import json

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/" \
          "watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if not response.ok:
        return None

    response_dict = json.loads(response.text)

    emotions = response_dict["emotionPredictions"][0]["emotion"]

    required_emotions = {
        "anger": emotions.get("anger", 0),
        "disgust": emotions.get("disgust", 0),
        "fear": emotions.get("fear", 0),
        "joy": emotions.get("joy", 0),
        "sadness": emotions.get("sadness", 0)
    }

    dominant_emotion = max(required_emotions, key=required_emotions.get)

    return {
        "anger": required_emotions["anger"],
        "disgust": required_emotions["disgust"],
        "fear": required_emotions["fear"],
        "joy": required_emotions["joy"],
        "sadness": required_emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }