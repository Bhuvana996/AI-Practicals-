from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

x = ["win money", "hello friend", "claim prize", "good morning"]
y = ["Spam", "Not Spam", "Spam", "Not Spam"]

v = CountVectorizer()
X = v.fit_transform(x)

model = MultinomialNB()
model.fit(X, y)

msg = v.transform(["win prize"])
print("Prediction:", model.predict(msg)[0])
