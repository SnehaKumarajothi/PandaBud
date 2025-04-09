from flask import Flask, request, jsonify, render_template
import joblib
import pickle
from predictEmotionLib import predictEmotion



app = Flask(__name__)

# Emotion-to-image/quote mapping
emotion_data = {
    "sadness": {
        "image": "https://drive.google.com/file/d/174S-CW3wU5pKXv_zYwVAE1sYE-pLbnyF/preview",
        "quote": "Tears come from the heart, not the brain."
    },
    "joy": {
        "image": "https://drive.google.com/file/d/1nMxA8inrxPcDOcyddOFMtg6x84a07vKa/preview",
        "quote": "Joy is not in things; it is in us."
    },
    "love": {
        "image": "https://drive.google.com/file/d/1qKBNh6Uupc4Ee5SGLDouw9wrRSJ3m737/preview",
        "quote": "Love is the only force capable of transforming an enemy into a friend."
    },
    "anger": {
        "image": "https://drive.google.com/file/d/1owCSDMdxKw9Gd8_HT7VR2ttNKDFA9lHU/preview",
        "quote": "Speak when you are angry and you’ll make the best speech you’ll ever regret."
    },
    "fear": {
        "image": "https://drive.google.com/file/d/1NgUsir6v1RJEM7s8PASqGsWRV3ysm9_I/preview",
        "quote": "Do one thing every day that scares you."
    },
    "surprise": {
        "image": "https://drive.google.com/file/d/16pxCV8lEGNCrTSRkbUPZmb-fQlVZ6Ktp/preview",
        "quote": "Life is full of surprises, but the biggest one is discovering yourself."
    }
}


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['message']
    modelName = data['model']

    emotion = predictEmotion(text, modelName)
    return jsonify({
        'emotion': emotion,
        'image_url': emotion_data[emotion]['image'],
        'quote': emotion_data[emotion]['quote']
    })

if __name__ == '__main__':
    app.run(debug=True)
