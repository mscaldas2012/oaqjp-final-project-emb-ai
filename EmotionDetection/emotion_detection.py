import requests

def emotion_detector(text_to_analyze):
    """
    This method uses Watson to analyze the text passed as parameter.
    It uses the Emotion Predict function of the Watson NLP Library.

    :param text_to_analyze: text to be analyzed
    :return:  the emotion with the highest score received from the Emotion Detection service.
    """

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        'Content-Type': 'application/json',
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'
    }
    payload = {
        'raw_document': {
            'text': text_to_analyze
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
         # Check for status code 400
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        response.raise_for_status()  # Raise an exception for bad status codes
        #extract emotion predictions
        emotion_predictions = response.json()['emotionPredictions'][0]['emotion'] 
        
        dominant_emotion = max(emotion_predictions.items(), key=lambda x: x[1])[0]

        result = {
            'anger': emotion_predictions['anger'],
            'disgust': emotion_predictions['disgust'],
            'fear': emotion_predictions['fear'],
            'joy': emotion_predictions['joy'],
            'sadness': emotion_predictions['sadness'],
            'dominant_emotion': dominant_emotion
        }
        return result

    except requests.exceptions.RequestException as e:
        return {
            'error_message': str(e)
        } 

if __name__ == "__main__":
    print(emotion_detector("I love this new tech"))  