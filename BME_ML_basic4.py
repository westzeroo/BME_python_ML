# BME_ML_basic4

from matplotlib import pyplot as plt
import numpy as np

# Basic Plotting
x = np.arange(10) # x = range(10)
y = x
plt.plot(x,y)
# Optional (decoration)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line plotting')
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.grid()
#decorate
plt.plot(x, y, color='red', marker='o',linestyle='dashed')
plt.show()

# Multiple Plotting
x = np.arange(0,10,0.1)
y = np.sin(x)
z = np.cos(x)
# plt.plot(x, y)
# plt.plot(x, z)
plt.plot(x,y,x,z)
# plt.legend(['sine','cosine'], loc='upper right') # legend: upper right
plt.legend(['sine','cosine'], loc=1) # legend: upper right
plt.show()
# lengend has location code(such as 1)

Multiple Subplots
plt.subplot(2,2,1) # First subplot in 2 x 2 subplots (Top-left)
plt.subplot(2,2,2) # Second subplot in 2 x 2 subplots (Top-right)
plt.subplot(2,2,3) # Third subplot in 2 x 2 subplots (Bottom-left)
plt.subplot(2,2,4) # Fourth subplot in 2 x 2 subplots (Bottom-right)
plt.show()

plt.subplot(1,2,1) # First subplot in 1 x 2 subplots
plt.plot(x,y)
plt.subplot(1,2,2) # Second subplot in 1 x 2 subplots
plt.plot(x,z)
plt.show()

plt.subplot(1,2,1) # First subplot in 1 x 2 subplots
plt.plot(x,y,'r')
plt.grid()
plt.xlabel('x')
plt.ylabel('sine(x)')
plt.title('Sine Graph')
plt.subplot(1,2,2) # Second subplot in 1 x 2 subplots
plt.plot(x,z,'g')
plt.grid()
plt.xlabel('y')
plt.ylabel('cosine(y)')
plt.title('Cosine Graph')
plt.tight_layout()
plt.show()

s = np.tan(x)
plt.subplot(3,3,1)  # (3*3 row*column image, 1 (=index))
plt.plot(x,x)
plt.subplot(3,3,2)  # (3*3 row*column image, 2 (=index))
plt.plot(x,z)
plt.subplot(3,3,3)  # (3*3 row*column image, 3 (=index))
plt.plot(x,s)
plt.subplot(3,3,4)  # (3*3 row*column image, 4 (=index))
plt.plot(y,y)
plt.subplot(3,3,5)  # (3*3 row*column image, 5 (=index))
plt.plot(s,y)
plt.subplot(3,3,6)  # (3*3 row*column image, 6 (=index))
plt.plot(x,y)
plt.subplot(3,3,7)  # (3*3 row*column image, 7 (=index))
plt.plot(x,y)
plt.subplot(3,3,8)  # (3*3 row*column image, 8 (=index))
plt.plot(x,y)
plt.subplot(3,3,9)  # (3*3 row*column image, 9 (=index))
plt.plot(x,y)
plt.tight_layout()      # there are distance between graphs
plt.show()

# Basic methods from Pandas
import pandas as pd
df = pd.read_csv("titanic.csv")
type(df)
print(type(df))
print(df)
print(df.head())
print(df.head(3))
print(df.tail())
print(df.tail(3))
print(df.columns)
print(df.index)

# Data frame sclicing
# df[column names][index]
df1 = df[['Survived','Name','Sex','Age']]
print(df1)
df2 = df[['Survived','Name','Sex','Age']][227:235]
print(df2)

# Data processing
# handling missing information
print(df.head())
df = df.drop(['PassengerId', 'Name', 'Ticket'], axis=1)
print(df.head())

print(df.isna()) # input.isnull() also works.
print(df.isna().sum(axis=0))

# data imputation
# about 'age'
age_mean = df['Age'].mean()
df1 = df['Age'].fillna(age_mean)
print(df1)
# confirm the number of missing information
print(df1.isna().sum())
# using parameter
df['Age'].fillna(age_mean, inplace=True)
print(df)
# about 'cabin'
print(df.isna().sum())
# about missing percent
print(687/891*100) # decide to drop
df.drop('Cabin', axis=1, inplace=True)
print(df)
print(df.isna().sum())
# about 'Embarked'
# .dropna(subset = ['column']); 해당 column의 값이 nan이면 줄 삭제
df.dropna(subset=['Embarked'], inplace=True)
print(df)
print(df.isna().sum())

# one hot encoding
# about 'sex'
# method 'unique()'
print(df['Sex'].unique())
# method "value_counts( )"
print(df['Sex'].value_counts())
# method 'pd.get_dummies(data frame, original column)' 
df = pd.get_dummies(df, columns = ['Sex'], dtype=int)
# df = pd.get_dummies(df, columns = ['Sex'])하면 error라 dytype 추가
print(df)
# about "Embarked"
print(df['Embarked'].unique())
print(df['Embarked'].value_counts())
df = pd.get_dummies(df, columns=['Embarked'], dtype=int)
print(df)

# about input / output data
label = df[['Survived']]
input = df.drop('Survived', axis=1)
print(label.head())
print(input.head())

# Data split
# import a specific method only from a package
# A sklearn package is divided into multiple modules, and one of them is model_selection.
# In model_selection, we will use train_test_split( ) method.
from sklearn.model_selection import train_test_split
train_data, test_data, train_label, test_label = train_test_split(input, label, test_size=0.2, stratify=label, random_state=1)
print(train_data)
print(train_data.shape)
print(train_label.shape)
print(test_data.shape)
print(test_label.shape)
# confirm splitted data
print(178/889*100)
# column data
column_data = train_data.columns
print(column_data)
print(len(column_data))
# confirm label proportion
# training data
n_total = train_label['Survived'].shape[0]
n_survived = train_label['Survived'].sum()
n_deceased = n_total - n_survived
mortality_rate = n_deceased/n_total * 100
print(f"Survied passenges: {n_survived}")
print(f"Deceased passenges: {n_deceased}")
print(f"Mortality rate:: {mortality_rate:.2f}%")
# testing data
n_total = test_label['Survived'].shape[0]
n_survived = test_label['Survived'].sum()
n_deceased = n_total - n_survived
mortality_rate = n_deceased/n_total * 100
print(f"Survied passenges: {n_survived}")
print(f"Deceased passenges: {n_deceased}")
print(f"Mortality rate:: {mortality_rate:.2f}%")


# Data Scaling
print(train_data.describe())
# standardscaler
from sklearn.preprocessing import StandardScaler
ss = StandardScaler() # object
ss.fit(train_data)
train_data_ss = ss.transform(train_data)
test_data_ss = ss.transform(test_data) # Given the mean and std from the training data
train_data_ss = pd.DataFrame(train_data_ss, columns=column_data)
print(train_data_ss)
print(train_data_ss.describe())
train_data_ss = pd.DataFrame(train_data_ss, columns=column_data)
print(train_data_ss)

# minmaxscaler
from sklearn.preprocessing import MinMaxScaler
mm = MinMaxScaler()
mm.fit(train_data)
train_data_mm = mm.transform(train_data)
test_data_mm = mm.transform(test_data) # Given the min and max from the training data
train_data_mm = pd.DataFrame(train_data_mm, columns=column_data)
print(train_data_mm)
train_data_mm.describe()
test_data_mm = pd.DataFrame(test_data_mm, columns=column_data)
test_data_mm.describe()

Machine learning models
logistic regression
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(train_data_ss, train_label)
accuracy_train = lr.score(train_data_ss,train_label)
print(f"Training data accuracy is {accuracy_train*100:.2f}%")
accuracy_test = lr.score(test_data_ss,test_label)
print(f"Test data accuracy is {accuracy_test*100:.2f}%")

# support vector machine
from sklearn.svm import SVC
svc = SVC()
svc.fit(train_data_ss, train_label)
accuracy_train = svc.score(train_data_ss,train_label)
print(f"Training data accuracy is {accuracy_train*100:.2f}%")
accuracy_test = svc.score(test_data_ss,test_label)
print(f"Test data accuracy is {accuracy_test*100:.2f}%")

# decision tree
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(train_data_ss, train_label)
accuracy_train = dt.score(train_data_ss,train_label)
print(f"Training data accuracy is {accuracy_train*100:.2f}%")
accuracy_test = dt.score(test_data_ss,test_label)
print(f"Test data accuracy is {accuracy_test*100:.2f}%")

# random forest
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(train_data_ss, train_label)
accuracy_train = rf.score(train_data_ss,train_label)
print(f"Training data accuracy is {accuracy_train*100:.2f}%")
accuracy_test = rf.score(test_data_ss,test_label)
print(f"Test data accuracy is {accuracy_test*100:.2f}%")

# Adaboost
from sklearn.ensemble import AdaBoostClassifier
ab = AdaBoostClassifier()
ab.fit(train_data_ss, train_label)
accuracy_train = ab.score(train_data_ss,train_label)
print(f"Training data accuracy is {accuracy_train*100:.2f}%")
accuracy_test = ab.score(test_data_ss,test_label)
print(f"Test data accuracy is {accuracy_test*100:.2f}%")

