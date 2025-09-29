from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Format for the return statement
    scores_printed = ", ".join(f"'{k}': {response[k]}" for k in response if k != 'dominant_emotion')

    # Extract the dominant emotion from the response
    dominant_emo = response['dominant_emotion']

    # Handle blank entries
    if dominant_emo is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with all emotion scores and dominant emotion    
    return f"For the given statement, the system response is {scores_printed}. The dominant emotion is {dominant_emo}"

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)