import pandas as pd
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'

raw_data_train = pd.read_csv('./data/train.csv')
raw_data_train.info()

train_pre = raw_data_train[['CPU', 'MEMORY','STORAGE','RATING']]
train_pre.head()

raw_data_test = pd.read_csv('./data/test.csv')
raw_data_test.info()

test_pre = raw_data_test[['CPU', 'MEMORY','STORAGE','RATING']]
test_pre.head()

X_train = train_pre
X_test = test_pre
y_train = raw_data_train['SCALE']
y_test = raw_data_test['SCALE']

from sklearn.tree import DecisionTreeClassifier
tree_clf = DecisionTreeClassifier(max_depth=3, random_state=13)
tree_clf.fit(X_train, y_train)
print('Score: {}'.format(tree_clf.score(X_train, y_train)))

from sklearn.tree import export_graphviz

export_graphviz(
        tree_clf,
        out_file="resource.dot",
        feature_names=['CPU', 'MEMORY', 'STORAGE', 'RATING'],
        class_names=['Unchange','scale-up','scale-down'],
        rounded=True,
        filled=True
    )


import graphviz
print(graphviz.__version__)
with open("resource.dot") as f:
    dot_graph = f.read()
dot = graphviz.Source(dot_graph)
dot.format = 'png'
dot.render(filename='resource', cleanup=True)
dot