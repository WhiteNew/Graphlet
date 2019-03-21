import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  
from sklearn.model_selection import train_test_split  
from sklearn.svm import SVC  
from sklearn.metrics import classification_report, confusion_matrix 


if __name__=="__main__":
   
# Assign colum names to the dataset
    colnames = ['soureIP', 'destIP', 'protocol', 'sPort', 'sPort', 'result']

# Read dataset to pandas dataframe
    irisdata = pd.read_csv("annotated-trace.csv", names=colnames)  
    X = irisdata.drop('result', axis=1)  
    y = irisdata['result']  

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.10)  

    svclassifier = SVC(kernel='poly', degree=10)  
    svclassifier.fit(X_train, y_train)  
    y_pred = svclassifier.predict(X_test)
    
    print(confusion_matrix(y_test, y_pred))  
    print(classification_report(y_test, y_pred))
    mydata = pd.read_csv("not-annotated-trace.csv")
    mytest=svclassifier.predict(X_train)
    f = open('resultdata.txt','w')
    for result in mytest:
        f.write(result+'\n')
    f.close