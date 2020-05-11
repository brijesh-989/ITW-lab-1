
 
# Python version
import sys

# scipy
import scipy


# scikit-learn
import sklearn


# Load libraries

from matplotlib import pyplot as plt
from numpy import *
from pandas import *
from pandas.plotting import scatter_matrix

from sklearn.model_selection import train_test_split

from sklearn.svm import SVC





# Load dataset

dataset = read_csv("Problem2.csv")

# Split-out validation dataset
array = dataset.values
X = array[:,0:8]
y = array[:,8]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20, random_state=1)




from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


svc = SVC(gamma='auto')
svc.fit(X_train, y_train)


print()
print()

print('Accuracy  on training dataset: {:.5f}'
     .format(svc.score(X_train, y_train)))
print()

print('Accuracy  on testing dataset: {:.5f}'
     .format(svc.score(X_test, y_test)) )

print()
print()






# box and whisker plots
dataset.drop('Outcome' ,axis=1).plot(kind='box', subplots=True, layout=(4,4), sharex=False, sharey=False,figsize=(15,15),title='Box Plot for each input variable')

plt.show()



dataset.drop('Outcome' ,axis=1).hist(bins=30, figsize=(15,15))
plt.suptitle("Histogram for each numeric input variable")

plt.show()




# scatter plot matrix
scatter_matrix(dataset,figsize=(18,18),hist_kwds={'bins':15})
plt.show()









