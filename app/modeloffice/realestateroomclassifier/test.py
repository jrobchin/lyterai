from classifier import RealEstateImageClassifier

print("Loading model...")
cls = RealEstateImageClassifier()
print("Done loading")

url = "http://www.14wctoh.org/wp-content/uploads/2017/11/kitchen-featured.jpg"
print("Processing", url, "...")
fp = cls.preprocess("http://www.14wctoh.org/wp-content/uploads/2017/11/kitchen-featured.jpg")
print("Done processing", fp)

print("Making a prediction...")
prediction, confidence = cls.predict(image_path=fp)
print("Done predicting", prediction, confidence)

