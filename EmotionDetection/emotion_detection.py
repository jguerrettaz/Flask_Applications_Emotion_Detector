import requests
import json

def emotion_detector(text_to_analyze):
    '''Function to assess the emotion of a text string'''

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = my_obj, headers = headers)

    # Handle blank entries
    if response.status_code == 400:
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    # Get dictionary of emotion scores from response.text
    response_f = json.loads(response.text)
    emo_scores = response_f['emotionPredictions'][0]['emotion']

    # Get emotion with the highest score
    sorted_emo_scores = sorted(emo_scores.items(), key = lambda item: item[1], reverse = True)
    dominant_emo = sorted_emo_scores[0][0]

    # Add dominant emotion to scores dictionary
    emo_scores['dominant_emotion'] = dominant_emo

    return emo_scores