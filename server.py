"""
Emotion text detector for IBM's AI course using Flask
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

# Set index route
@app.route('/')
def render_index_page():
    """
    Render index page
    """
    return render_template('index.html')

# Define route for app
@app.route('/emotionDetector')
def detector():
    """
        Get text and send to emotion_detector
        Set dominant_emotion of response dict to variable
    """
    text_to_analyze = request.args.get('textToAnalyze')

    resp = emotion_detector(text_to_analyze)
    dominant_emotion = resp['dominant_emotion']

    if resp is None or resp['dominant_emotion'] is None:
        return "Invalid input, please try again."

    return f"For the given statement, the system response is {resp}. \
        The dominant emotion is {dominant_emotion}."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
