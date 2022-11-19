from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.naive_bayes import *
from sklearn.ensemble import RandomForestClassifier


class class_SVM:
    X = []
    y = []
    model = None

    def __init__(self, data, label):
        self.X = data
        self.y = label

    def viewDataset(self):
        print("data :", self.X)
        print("label :", self.y)

    def model(self):
        # print("in model X :", self.X)
        # print(len(self.X))
        self.model = svm.SVR()
        self.model.fit(np.array(self.X), self.y)

    def predict(self, data_testing):
        # print("prediksi : ", self.model.predict(data_testing))
        print(data_testing)
        return self.model.predict(data_testing)
class class_NB:
    X = []
    y = []
    model = None

    def __init__(self, data, label):
        self.X = data
        self.y = label

    def viewDataset(self):
        print("data :", self.X)
        print("label :", self.y)

    def model(self):
        # print("in model X :", self.X)
        # print(len(self.X))
        self.model = GaussianNB()
        self.model.fit(np.array(self.X), self.y)

    def predict(self, data_testing):
        # print("prediksi : ", self.model.predict(data_testing))
        return self.model.predict(data_testing)

class class_KNN:
    X = []
    y = []
    model = None

    def __init__(self, data, label):
        self.X = data
        self.y = label

    def viewDataset(self):
        print("data :", self.X)
        print("label :", self.y)

    def model(self,n_neighbors):
        # print("in model X :", self.X)
        # print(len(self.X))
        self.model = KNeighborsClassifier(n_neighbors=n_neighbors)
        self.model.fit(np.array(self.X), self.y)

    def predict(self, data_testing):
        # print("prediksi : ", self.model.predict(data_testing))
        return self.model.predict(data_testing)

class class_MNB:
    X = []
    y = []
    model = None

    def __init__(self, data, label):
        self.X = data
        self.y = label

    def viewDataset(self):
        print("data :", self.X)
        print("label :", self.y)

    def model(self):
        # print("in model X :", self.X)
        # print(len(self.X))
        self.model = MultinomialNB()
        self.model.fit(np.array(self.X), self.y)

    def predict(self, data_testing):
        # print("prediksi : ", self.model.predict(data_testing))
        print(data_testing)
        return self.model.predict(data_testing)

class class_rfc:
    X = []
    y = []
    model = None

    def __init__(self, data, label):
        self.X = data
        self.y = label

    def viewDataset(self):
        print("data :", self.X)
        print("label :", self.y)

    def model(self):
        # print("in model X :", self.X)
        # print(len(self.X))
        self.model = RandomForestClassifier(n_estimators=10)
        self.model.fit(np.array(self.X), self.y)

    def predict(self, data_testing):
        # print("prediksi : ", self.model.predict(data_testing))
        print(data_testing)
        return self.model.predict(data_testing)

class class_bnb:
    X = []
    y = []
    model = None

    def __init__(self, data, label):
        self.X = data
        self.y = label

    def viewDataset(self):
        print("data :", self.X)
        print("label :", self.y)

    def model(self):
        # print("in model X :", self.X)
        # print(len(self.X))
        self.model = BernoulliNB()
        self.model.fit(np.array(self.X), self.y)

    def predict(self, data_testing):
        # print("prediksi : ", self.model.predict(data_testing))
        print(data_testing)
        return self.model.predict(data_testing)