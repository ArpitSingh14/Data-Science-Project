# -*- coding: utf-8 -*-
"""covid-19.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cN9IHCMcqJEfcRssJWmwDCcvJ-b1Dks3
"""

from google.colab import files
uploaded=files.upload()

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import time
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report,confusion_matrix, roc_auc_score, mean_squared_error,r2_score, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.ensemble import RandomForestRegressor

covid_data=pd.read_csv("Covid Dataset.csv")
print(covid_data.columns)

Yes_count=covid_data['COVID-19'].value_counts().get('Yes',0)
print("Number of rows with 'yes':",Yes_count)
no_count=covid_data['COVID-19'].value_counts().get('No',0)
print("Number of rows with 'no':",no_count)

print(covid_data.info)

print(covid_data.describe().T)

missing_values = covid_data.isnull().sum
print(missing_values)

percent_missing = covid_data.isnull().sum() * 100 / len(covid_data)
print(percent_missing)

value ={
    'missing_values':missing_values,
    'percent_missing ':percent_missing
}
missing_data=pd.DataFrame(value)
(missing_data)

sns.heatmap(covid_data.isnull(),yticklabels=False,cbar=False,cmap='Pastel1')

ax=sns.countplot(x='Hyper Tension',hue='COVID-19',data=covid_data,palette='Set1')
for p in ax.patches:
  ax.annotate(f'\n{p.get_height()}',(p.get_x()+0.4,p.get_height()+100),ha='center',va='top',color='black',size=15)
  plt.show()

ax=sns.countplot(x='Fever',hue='COVID-19',data=covid_data,palette='Set1')
for p in ax.patches:
  ax.annotate(f'\n{p.get_height()}',(p.get_x()+0.4,p.get_height()+100),ha='center',va='top',color='black',size=15)
  plt.show()

ax=sns.countplot(x='Wearing Masks',hue='COVID-19',data=covid_data,palette='Set1')
for p in ax.patches:
  ax.annotate(f'\n{p.get_height()}',(p.get_x()+0.4,p.get_height()+100),ha='center',va='top',color='black',size=15)
  plt.show()

ax=sns.countplot(x='Dry Cough',hue='COVID-19',data=covid_data,palette='Set1')
for p in ax.patches:
  ax.annotate(f'\n{p.get_height()}',(p.get_x()+0.4,p.get_height()+100),ha='center',va='top',color='black',size=15)
  plt.show()

ax=sns.countplot(x='Sore throat',hue='COVID-19',data=covid_data,palette='Set1')
for p in ax.patches:
  ax.annotate(f'\n{p.get_height()}',(p.get_x()+0.4,p.get_height()+100),ha='center',va='top',color='black',size=15)
  plt.show()

ax=sns.countplot(x='Diabetes',hue='COVID-19',data=covid_data,palette='Set1')
for p in ax.patches:
  ax.annotate(f'\n{p.get_height()}',(p.get_x()+0.4,p.get_height()+100),ha='center',va='top',color='black',size=15)
  plt.show()

ax=sns.countplot(x='Chronic Lung Disease',hue='COVID-19',data=covid_data,palette='Set1')
for p in ax.patches:
  ax.annotate(f'\n{p.get_height()}',(p.get_x()+0.4,p.get_height()+100),ha='center',va='top',color='black',size=15)
  plt.show()

ax=sns.countplot(x='Abroad travel',hue='COVID-19',data=covid_data,palette='Set1')
for p in ax.patches:
  ax.annotate(f'\n{p.get_height()}',(p.get_x()+0.4,p.get_height()+100),ha='center',va='top',color='black',size=15)
  plt.show()

ax=sns.countplot(x='Contact with COVID Patient',hue='COVID-19',data=covid_data,palette='Set1')
for p in ax.patches:
  ax.annotate(f'\n{p.get_height()}',(p.get_x()+0.4,p.get_height()+100),ha='center',va='top',color='black',size=15)
  plt.show()

ax=sns.countplot(x='Family working in Public Exposed Places',hue='COVID-19',data=covid_data,palette='Set1')
for p in ax.patches:
  ax.annotate(f'\n{p.get_height()}',(p.get_x()+0.4,p.get_height()+100),ha='center',va='top',color='black',size=15)
  plt.show()

e = LabelEncoder()
#covid_data['Breathing Problem']=e.fit_transform(covid_data['Breathing Problem'])
covid_data['Fever']=e.fit_transform(covid_data['Fever'])
covid_data['Dry Cough']=e.fit_transform(covid_data['Dry Cough'])
covid_data['Sore throat']=e.fit_transform(covid_data['Sore throat'])
#covid_data['Running Nose']=e.fit_transform(covid_data['Running Nose'])
#covid_data['Asthma']=e.fit_transform(covid_data['Asthma'])
covid_data['Chronic Lung Disease']=e.fit_transform(covid_data['Chronic Lung Disease'])
#covid_data['Headache']=e.fit_transform(covid_data['Headache'])
#covid_data['Heart Disease']=e.fit_transform(covid_data['Heart Disease'])
covid_data['Diabetes']=e.fit_transform(covid_data['Diabetes'])
#covid_data['Hyper Tension']=e.fit_transform(covid_data['Hyper Tension'])
covid_data['Abroad travel']=e.fit_transform(covid_data['Abroad travel'])
covid_data['Contact with COVID Patient']=e.fit_transform(covid_data['Contact with COVID Patient'])
#covid_data['Attended Large Gathering']=e.fit_transform(covid_data['Attended Large Gathering'])
#covid_data['Visited Public Exposed Places']=e.fit_transform(covid_data['Visited Public Exposed Places'])
covid_data['Family working in Public Exposed Places']=e.fit_transform(covid_data['Family working in Public Exposed Places'])
covid_data['Wearing Masks']=e.fit_transform(covid_data['Wearing Masks'])
#covid_data['Sanitization from Market']=e.fit_transform(covid_data['Sanitization from Market'])
#covid_data['COVID-19']=e.fit_transform(covid_data['COVID-19'])
#covid_data['Dry Cough']=e.fit_transform(covid_data['Dry Cough'])
#covid_data['Sore throat']=e.fit_transform(covid_data['Sore throat'])
#covid_data['Gastrointestinal ']=e.fit_transform(covid_data['Gastrointestinal '])
#covid_data['Fatigue ']=e.fit_transform(covid_data['Fatigue '])

covid_data.head()
covid_data.hist(figsize=(20,15))
plt.show()

print(covid_data['Wearing Masks'].value_counts())
sns.countplot(x='Wearing Masks',data=covid_data)
plt.show()

print(covid_data['Dry Cough'].value_counts())
sns.countplot(x='Dry Cough',data=covid_data)
plt.show()

print(covid_data['Contact with COVID Patient'].value_counts())
sns.countplot(x='Contact with COVID Patient',data=covid_data)
plt.show()

plt.figure(figsize=(25,20))
sns.heatmap(covid_data.corr(), annot=True, cmap="PuRd")
plt.show()

x = covid_data.drop('COVID-19',axis=1)
y = covid_data['COVID-19']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 101)

from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(x_train, y_train)

y_pred = rf_model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)

print(f"Mean Squared Error: {mse}")

df=pd.DataFrame({'Actual Cases': y_test, 'Predicted Cases': y_pred})
df1 = df.head(25)
df1.plot(kind='bar',figsize=(19,9))

# Step 5: Predict cases and evaluate
y_pred = rf_model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)

print(f"Mean Squared Error: {mse}")

df=pd.DataFrame({'Actual Cases': y_test, 'Predicted Cases': y_pred})
df