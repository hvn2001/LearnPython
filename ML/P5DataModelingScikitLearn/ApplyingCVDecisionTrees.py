from sklearn import tree
from sklearn.model_selection import cross_val_score
import pandas as pd

is_clf = True  # for classification
data = pd.DataFrame([[2100, 800],
                     [2500, 850],
                     [1800, 760],
                     [2000, 800],
                     [2300, 810]],
                    )
# labels = pd.DataFrame([10, 10, 10, 10, 11]).values.ravel()  # ValueError: n_splits=5 cannot be greater than the number of members in each class.
labels = pd.DataFrame([10, 10, 10, 10, 10]).values.ravel()


def cv_decision_tree(is_clf, data, labels, max_depth, cv):
    if is_clf:
        d_tree = tree.DecisionTreeClassifier(max_depth=max_depth)
    else:
        d_tree = tree.DecisionTreeRegressor(max_depth=max_depth)
    scores = cross_val_score(d_tree, data, labels, cv=cv)
    return scores


for depth in range(3, 8):
    # Predefined data and labels
    scores = cv_decision_tree(
        is_clf, data, labels, depth, 5)  # k = 5
    mean = scores.mean()  # Mean acc across folds
    std_2 = 2 * scores.std()  # 2 std devs
    print('95% C.I. for depth {}: {} +/- {:.2f}\n'.format(
        depth, mean, std_2))
'''
95% C.I. for depth 3: 0.9201583773270352 +/- 0.03

95% C.I. for depth 4: 0.9234370658516253 +/- 0.06

95% C.I. for depth 5: 0.9266592572010743 +/- 0.02

95% C.I. for depth 6: 0.9232694266925998 +/- 0.03

95% C.I. for depth 7: 0.9168250439937019 +/- 0.04
'''
