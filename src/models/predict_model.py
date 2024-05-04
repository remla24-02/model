"""
Use trained models to make predictions.
"""

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns
import numpy as np
from joblib import load


def main():
    """
    Make predictions with the defined model.
    """
    model = load('models/trained_model.joblib')

    x_test = load('output/preprocessed_x_test.joblib')
    y_test = load('output/preprocessed_y_test.joblib')

    # Make predictions
    y_pred = model.predict(x_test, batch_size=1000)
    print(y_pred)

    # Convert predicted probabilities to binary labels
    y_pred_binary = (np.array(y_pred) > 0.5).astype(int)
    y_test = y_test.reshape(-1, 1)

    # Calculate classification report
    report = classification_report(y_test, y_pred_binary)
    print('Classification Report:')
    print(report)

    # Calculate confusion matrix
    confusion_mat = confusion_matrix(y_test, y_pred_binary)
    print('Confusion Matrix:', confusion_mat)
    print('Accuracy:', accuracy_score(y_test, y_pred_binary))

    sns.heatmap(confusion_mat, annot=True)


if __name__ == "__main__":
    main()
