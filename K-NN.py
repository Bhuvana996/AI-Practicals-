from sklearn.neighbors import KNeighborsClassifier

X = [[1], [2], [3], [6], [7], [8]]
y = ["Fail", "Fail", "Fail", "Pass", "Pass", "Pass"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

print("Prediction:", model.predict([[5]])[0])
print("Accuracy:", model.score(X, y))
