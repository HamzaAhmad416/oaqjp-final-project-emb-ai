import requests

def emotion_detector(text_to_analyse):
    """
    Sends text to Watson Emotion API and returns formatted emotions
    """

    # ✅ API Endpoint (as given)
    url = "https://sn-watson-emotion.labs.skills.network/v1/" \
          "watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # ✅ Headers (as given)
    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    # ✅ Input JSON (as given)
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    # ✅ API Request
    response = requests.post(url, json=payload, headers=headers)

    # ✅ Error Handling (Task 7 requirement)
    if response.status_code == 400:
        return None

    # ✅ Convert response to JSON
    response_json = response.json()

    # ✅ Extract emotions
    emotions = response_json['emotionPredictions'][0]['emotion']

    # ✅ Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # ✅ Final formatted output (Task 3 requirement)
    return {
        "sadness": emotions["sadness"],
        "joy": emotions["joy"],
        "fear": emotions["fear"],
        "disgust": emotions["disgust"],
        "anger": emotions["anger"],
        "dominant_emotion": dominant_emotion
    }