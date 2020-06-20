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


# Initialize the models
clf_A = LogisticRegression(solver="sag", class_weight='balanced', multi_class="ovr")
clf_B = SVC(random_state=912, kernel='rbf')
clf_C = xgb.XGBClassifier(max_depth=3, objective='multi:softmax', n_estimators=50)
RF_clf = RandomForestClassifier(n_estimators=200, random_state=1, class_weight='balanced')
# GNB_clf = GaussianNB()


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


all_data = pd.read_csv('C:\\Users\\sfrei\\Desktop\\Degree\\Y03S02\\Project Preparation\\Part 5\\prepared_data.csv')


# train_predict(clf_A, train_features, train_target, test_features, test_target)
# print('')
# train_predict(clf_B, train_features, train_target, test_features, test_target)
# print('')
# train_predict(clf_C, train_features, train_target, test_features, test_target)
# print('')
# train_predict(RF_clf, train_features, train_target, test_features, test_target)
# print('')
# train_predict(GNB_clf, X_train, y_train, X_test, y_test)
# print('')

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
#
# feature_names = list(train_features.columns.values)
# rfecv = RFECV(clf_C, step=1, cv=10)
# rfecv = rfecv.fit(train_features, train_target)
# print("Features sorted by their rank:")
# print(sorted(zip(map(lambda x: round(x, 4), rfecv.ranking_), feature_names)))
#
#
# print('------------------------------------new----KNN----model------------------------------')
# KNN = KNeighborsClassifier()
# KNN_model = KNN.fit(train_features, train_target)
# KNN_preds = KNN.predict(test_features)
# print(accuracy_score(test_target, KNN_preds))