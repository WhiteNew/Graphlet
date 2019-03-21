# python3
# -*- coding: utf-8 -*-
# @Author  : bai xin
# @Time    : 2019-02-25 08:52
import pandas as pd
from sklearn.svm import SVC
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def read_csv(file_path, is_train):
    """
    get the csv data.
    :param file_path:
    :param is_train: train data or test data, is_train=1 if train data is.
    :return:
    """
    df = pd.read_csv(file_path)

    if is_train:   # train data
        features = ["soureIP", "destIP", "protocol", "sPort", "dPort"]
        data = df[features]
        class_mapping = {'anomaly': 1, 'normal': 0}
        label = df['result'].map(class_mapping)
        return [data, label]
    else:   # not annotated data
        return df


def classifier(X, y, not_annotated_data):
    """
    classifier model, evaluation and prediction not annotated data.
    :param X: annotated data.
    :param y: label of annotated data.
    :param not_annotated_data:
    :return: prediction result of not_annotated_data.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
    svc = SVC()
    svc.fit(X_train, y_train)
    y_test_predict = svc.predict(X_test)
    print(classification_report(y_test_predict, y_test, target_names=['1', '0']))

    prediction = svc.predict(not_annotated_data)
    return prediction


def visualize(not_annotated_data, prediction):
    """
    visualize after dimensionality reduction by t-SNE.
    :param not_annotated_data:
    :param prediction: prediction result.
    :return:
    """
    tsne = TSNE(n_components=2)
    tsne.fit_transform(np.array(not_annotated_data))
    reduced_data = tsne.embedding_
    # print(reduced_data)
    plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=prediction, marker='o', s=40)  # c--color，s--size,marker点的形状
    plt.show()


if __name__ == '__main__':
    train_file_path = "../data/annotated-trace.csv"
    test_file_path = "../data/not-annotated-trace.csv"
    [train_data, label] = read_csv(train_file_path, True)
    not_annotated_data = read_csv(test_file_path, False)
    #prediction = classifier(train_data, label, not_annotated_data)
    prediction = classifier(train_data, label, train_data)
    print(list(prediction).count(1))
    print(list(prediction).count(0))
    #visualize(not_annotated_data, prediction)
    visualize(train_data,prediction)
