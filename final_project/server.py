from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

# Set index route
@app.route('/')
def render_index_page():
    return render_template('index.html')

# Define route for app
@app.route('/emotionDetector')
def detector():
    text_to_analyze = request.args.get('textToAnalyze') # Get text
    # Send text to emotion detect function
    resp = emotion_detector(text_to_analyze)
    # Set dominant_emotion of response dict to variable
    dom_emotion = resp['dominant_emotion'] 

    if resp is None or resp.get('anger') is None:
        return "Invalid input, please try again."
    else:
        return f"For the given statement, the system response is {resp}. The dominant emotion is {dom_emotion}."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)