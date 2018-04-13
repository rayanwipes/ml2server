from sklearn import metrics
import matplotlib.pyplot as plt

def generate_recall_graph(y_val, y_predicted, title):
    plt.switch_backend('agg')
    precision, recall, _ = metrics.precision_recall_curve(y_val, y_predicted)

    plt.step(recall, precision, color='b', alpha=0.2, where='post')
    plt.fill_between(recall, precision, step='post', alpha=0.2, color='b')

    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.title(title)
    plt.show()