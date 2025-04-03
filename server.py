# pylint: disable=E0401
"""
#This the server which connects all modules to a specific route.

#Functions:
    - home,
    - emotionDetect
"""
from flask import Flask, request, render_template, jsonify
from final_project.emotion_detection import emotion_detector as ed

app = Flask("Final Project")

@app.route("/")
def home():
    """
    Function takes a text through body and
    returns the emotions it conveys and the most domminant.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotiondetect():
    """
    Function takes a text through body and returns
    the emotions it conveys and the most domminant.
    """
    data = request.get_json()
    text_to_analyze = data.get("text", "")
    result = ed(text_to_analyze)
    if result.get('dominant_emotion') is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}.\n"
    )
    return response_message
