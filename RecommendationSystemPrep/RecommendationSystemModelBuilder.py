from time import time
from sklearn.feature_selection import RFECV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, accuracy_score
import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer
from datetime import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import numpy as np


# train and test functions
def train_classifier(clf, X_train, y_train):
    ''' Fits a classifier to the training data. '''

    # Start the clock, train the classifier, then stop the clock
    start = time()
    clf.fit(X_train, y_train)
    end = time()

    # Print the results
    print("Trained model in {:.4f} seconds".format(end - start))


def predict_labels(clf, features, target):
    ''' Makes predictions using a fit classifier based on F1 score. '''

    # Start the clock, make predictions, then stop the clock
    start = time()
    y_pred = clf.predict(features)

    end = time()
    # Print and return results
    print("Made predictions in {:.4f} seconds.".format(end - start))

    return f1_score(target, y_pred, labels=['Win', 'Draw', 'Lose'], average='micro'), sum(target == y_pred) / float(
        len(y_pred))


def train_predict(clf, X_train, y_train, X_test, y_test):
    ''' Train and predict using a classifer based on F1 score. '''

    # Indicate the classifier and the training set size
    print("Training a {} using a training set size of {}. . .".format(clf.__class__.__name__, len(X_train)))

    # Train the classifier
    train_classifier(clf, X_train, y_train)

    # Print the results of prediction for both training and testing
    f1, acc = predict_labels(clf, X_train, y_train)
    print(f1, acc)
    print("F1 score and accuracy score for training set: {:.4f} , {:.4f}.".format(f1, acc))

    f1, acc = predict_labels(clf, X_test, y_test)
    print("F1 score and accuracy score for test set: {:.4f} , {:.4f}.".format(f1, acc))


def get_optimal_model(clf, X, y):

    rfecv = RFECV(clf, step=1, cv=10)
    rfecv = rfecv.fit(X, y)
    return rfecv


def show_statistics(rfecv, feature_names, title):

    print("Features sorted by their rank - {}:".format(title))
    print(sorted(zip(map(lambda x: round(x, 4), rfecv.ranking_), feature_names)))

    plt.figure(figsize=(12, 10))
    plt.title(title)
    plt.xlabel("Number of features selected")
    plt.ylabel("Cross validation score (nb of correct classifications)")
    plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
    for x, y in zip(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_):
        label = "{:.4f}".format(y)

        plt.annotate(label,  # this is the text
                     (x, y),  # this is the point to label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 10),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center

    plt.xticks(np.arange(0, 16, 1))

    plt.show()


# Initialize the models
clf_LR = LogisticRegression(solver="sag", class_weight='balanced', multi_class="ovr")
clf_SVC = SVC(random_state=912, kernel='rbf')
clf_XGB = xgb.XGBClassifier(max_depth=3, objective='multi:softmax', n_estimators=50)
clf_RF = RandomForestClassifier(n_estimators=200, random_state=1, class_weight='balanced')
# GNB_clf = GaussianNB()

all_data = pd.read_csv('C:\\Users\\sfrei\\Desktop\\Degree\\Y03S02\\Project Preparation\\Part 5\\prepared_data.csv')
all_data['date'] = pd.to_datetime(all_data['date'])

test_start_date = datetime(2015, 1, 1)
test_end_date = datetime(2016, 12, 31)
train_start_date = test_start_date - relativedelta(years=3)

train = all_data[(all_data['date'] < test_start_date)]
test = all_data[((all_data['date'] >= test_start_date) & (all_data['date'] <= test_end_date))]

train_features = train.drop(['label'], 1)
train_features = train_features.drop(['date'], 1)
test_features = test.drop(['label'], 1)
test_features = test_features.drop(['date'], 1)
test_target = test['label']
train_target = train['label']

feature_names = list(train_features.columns.values)

rfecv_LR = get_optimal_model(clf_LR, train_features, train_target)
rfecv_XGB = get_optimal_model(clf_XGB, train_features, train_target)
rfecv_RF = get_optimal_model(clf_RF, train_features, train_target)

show_statistics(rfecv_LR, feature_names, "Logistic Regression")
show_statistics(rfecv_XGB, feature_names, "XGBoost")
show_statistics(rfecv_RF, feature_names, "Random Forest")

opt_LR_train = rfecv_LR.transform(train_features)
opt_LR_test = rfecv_LR.transform(test_features)
opt_XGB_train = rfecv_XGB.transform(train_features)
opt_XGB_test = rfecv_XGB.transform(test_features)
opt_RF_train = rfecv_RF.transform(train_features)
opt_RF_test = rfecv_RF.transform(test_features)


train_predict(clf_LR, opt_LR_train, train_target, opt_LR_test, test_target)
print('')
train_predict(clf_SVC, train_features, train_target, test_features, test_target)
print('')
train_predict(clf_XGB, opt_XGB_train, train_target, opt_XGB_test, test_target)
print('')
train_predict(clf_RF, opt_RF_train, train_target, opt_RF_test, test_target)
print('')

# train_predict(GNB_clf, X_train, y_train, X_test, y_test)
# print('')
#
# # tuning in XGBoost
# parameters = {'learning_rate': [0.1],
#               'n_estimators': [40],
#               'max_depth': [3],
#               'min_child_weight': [3],
#               'gamma': [0.4],
#               'subsample': [0.8],
#               'colsample_bytree': [0.8],
#               'reg_alpha': [1e-5]
#               }
# clf = xgb.XGBClassifier(seed=2)
# # Make an f1 scoring function using 'make_scorer'
# f1_scorer = make_scorer(f1_score, labels=['Win', 'Draw', 'Lose'], average='micro')
# # Perform grid search on the classifier using the f1_scorer as the scoring method
# grid_obj = GridSearchCV(clf, scoring=f1_scorer, param_grid=parameters, cv=5)
# # Fit the grid search object to the training data and find the optimal parameters
# grid_obj = grid_obj.fit(train_features, train_target)
# # Get the estimator
# clf = grid_obj.best_estimator_
# print(clf)
# # Report the final F1 score for training and testing after parameter tuning
# f1, acc = predict_labels(clf, train_features, train_target)
# print("F1 score and accuracy score for training set: {:.4f} , {:.4f}.".format(f1, acc))
# f1, acc = predict_labels(clf, test_features, test_target)
# print("F1 score and accuracy score for test set: {:.4f} , {:.4f}.".format(f1, acc))


# print('------------------------------------new----KNN----model------------------------------')
# KNN = KNeighborsClassifier()
# KNN_model = KNN.fit(train_features, train_target)
# KNN_preds = KNN.predict(test_features)
# print(accuracy_score(test_target, KNN_preds))