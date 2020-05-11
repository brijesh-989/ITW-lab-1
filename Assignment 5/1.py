

import scipy
import sklearn



from matplotlib import pyplot as plt
from numpy import *
from pandas import *
from pandas.plotting import scatter_matrix

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC






# Load dataset

dataset = read_table("Problem1.txt")


feature_names = ['mass', 'width', 'height', 'color_score']
X = dataset[feature_names]
y = dataset['fruit_label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)



from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)



logreg = LogisticRegression()
logreg.fit(X_train, y_train)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)


# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))

models.append(('KNN', KNeighborsClassifier()))

# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=4, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)


# Compare Algorithms
plt.boxplot(results, labels=names)
plt.title('Algorithm Comparison')
plt.show()

print()
print()

print('Accuracy of Logistic regression classifier on training dataset: {:.5f}'
     .format(logreg.score(X_train, y_train)) )


print('Accuracy of Logistic regression classifier on testing dataset: {:.5f}'
     .format(logreg.score(X_test, y_test)) )

print()
print()
print('Accuracy of K-NN classifier on training dataset: {:.5f}'
     .format(knn.score(X_train, y_train)) )
print('Accuracy of K-NN classifier on testing dataset: {:.5f}'
     .format(knn.score(X_test, y_test)))













# box and whisker plots
dataset.drop('fruit_label' ,axis=1).plot(kind='box', subplots=True, layout=(3,2), sharex=False, sharey=False,figsize=(9,9),title='Box Plot for each input variable')

plt.show()



dataset.drop('fruit_label' ,axis=1).hist(bins=30, figsize=(9,9))
plt.suptitle("Histogram for each numeric input variable")

plt.show()




from matplotlib import cm
feature_names = ['mass', 'width', 'height', 'color_score']
X = dataset[feature_names]
y = dataset['fruit_label']
cmap = cm.get_cmap('gnuplot')
scatter = scatter_matrix(X, c = y, marker = 'o', s=40, hist_kwds={'bins':15}, figsize=(9,9), cmap = cmap)
plt.suptitle('Scatter-matrix for each input variable')
plt.show()















