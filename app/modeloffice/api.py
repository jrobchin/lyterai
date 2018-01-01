from flask import Flask, request, jsonify
from keras import backend as K

from realestateroomclassifier.classifier import RealEstateImageClassifier

# Flask app
app = Flask(__name__)

# Models
models = {}

@app.route("/realestateclassifier", methods=['POST'])
def realestate():
    if request.method == 'POST':
        prediction, confidence = models["realestateclassifier"].predict(image_url=request.form['image-url'])
        return jsonify(prediction=prediction, confidence=confidence)

if __name__ == '__main__':
    K.clear_session()
    models["realestateclassifier"] = RealEstateImageClassifier()
    app.run(host='0.0.0.0', port=5000, debug=False)