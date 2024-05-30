from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def initialize_local_model():
    # Load a sample dataset
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

    # Train a simple model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the model to disk
    joblib.dump(model, 'local_model.pkl')

    # Return the trained model
    return model

def predict_with_local_model(model, data):
    # Prediction logic here
    return model.predict(data)
