from sklearn import metrics
import matplotlib.pyplot as plt


def generate_roc_graph(y_val, y_predicted, title):
    plt.switch_backend('agg')
    print("Receiver Operating Characteristics:")
    fpr, tpr, _ = metrics.roc_curve(y_val, y_predicted)
    print(fpr)
    print(tpr)

    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='orange', lw=lw, label='ROC curve')
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc='lower right')
    plt.show()
