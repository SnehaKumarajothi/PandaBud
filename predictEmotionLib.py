import joblib

def predictEmotion(text, modelName):
    vectorizer = joblib.load('models/tfidf_vectorizer.joblib')
    labels = ['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']

    model_paths = {
    'logistic': 'models/logistic_regression_model.joblib',
    'naive_bayes': 'models/naive_bayes_model.joblib',
    'svm': 'models/svm_model.joblib'
    }

    model_path = model_paths[modelName]
    model = joblib.load(model_path)
    text_vec = vectorizer.transform([text])
    pred = model.predict(text_vec)

    emotion = labels[pred[0]]
    return emotion

