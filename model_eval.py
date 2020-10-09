from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt


def draw_roc(y_true, y_probs, add_to_title=""):
    """Draw Receiver Operating Characteristic plot
    used to determine model performance.

    Args:
        y_true (list): True values for classes.
        y_probs (list): Probabilities for classes.
        add_to_title (str, optional): Additional text to add at the end of title
        . Defaults to "".
    """
    fpr, tpr, _ = roc_curve(y_true, y_probs)
    roc_auc = round(auc(fpr, tpr), 3)
    plt.figure()
    plt.plot([0, 1], [0, 1], color="navy", linestyle="--")
    plt.plot(fpr, tpr, color="red", label=f"ROC curve (area = {roc_auc})")
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(f"Receiver operating characteristic {add_to_title}")
    plt.legend(loc="lower right")
    plt.show()
