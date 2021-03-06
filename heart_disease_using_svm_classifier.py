# -*- coding: utf-8 -*-
"""Heart_disease_using_SVM_classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X8w5NEUyN7AXpIQWOEHEmtsVgtyHUHwk
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
# %matplotlib inline



from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

df=pd.read_csv('heart.csv')

df.head()

df.shape

df.describe()

df.info()

df.isnull().sum()

for i in df.columns:
    sns.distplot(df[i])
    plt.xlabel(i)
    plt.ylabel('Count')
    plt.show()

plt.figure(figsize=(12,10))
sns.heatmap(df.corr(),annot=True)

X = df.drop(['target'],axis=1)
y = df['target']

from sklearn.model_selection import train_test_split,cross_val_score

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.svm import SVC

svc=SVC()
svc.fit(X_train,y_train)

y_pred=svc.predict(X_test)

from sklearn.metrics import confusion_matrix,classification_report

print(confusion_matrix(y_test,y_pred))

print(classification_report(y_test,y_pred))

