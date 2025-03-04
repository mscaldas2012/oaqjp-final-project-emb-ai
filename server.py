"""
This module implements a Flask server for emotion detection.
It provides an endpoint that accepts text and returns detected emotions using Watson NLP.
"""
from flask import Flask, request, jsonify, Response
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetection", methods=['POST'])
def emotion_detection() -> tuple[Response, int]:
    """
    Endpoint for emotion detection in text.

    Returns:
        tuple: Contains JSON response and HTTP status code:
            - On error: ({'error': <message>}, 400)
            - On success: ({'response': <analysis>}, 200)
    """
    # Get text from request body
    text = request.data.decode('utf-8')

    # Call emotion detector
    result = emotion_detector(text)

    # Check if emotion was detected:
    if result['dominant_emotion'] is None:
        return jsonify({'error': 'Invalid text! Please try again!'}), 400

    # Check for errors
    if result.get('error'):
        return jsonify({'error': result['error']}), 400

    # Format response string
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({'response': response}), 200

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
    