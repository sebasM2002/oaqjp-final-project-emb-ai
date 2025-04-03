import requests
import json

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    payload = {"raw_document": {"text":text_to_analyze}}
    response = requests.post(URL, json=payload, headers=HEADERS)
    if response.status_code == 200:
        response_dict = json.loads(response.text)

        emotions = response_dict.get("emotionPredictions")[0].get("emotion")


        filtered_emotions = {
            "anger":emotions.get("anger"),
            "disgust": emotions.get("disgust"),
            "fear": emotions.get("fear"),
            "joy": emotions.get("joy"),
            "sadness": emotions.get("sadness")
        }
        dominant_emotion = max(filtered_emotions, key=filtered_emotions.get)

        filtered_emotions['dominant_emotion'] = dominant_emotion_

        return filtered_emotions
    elif response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }