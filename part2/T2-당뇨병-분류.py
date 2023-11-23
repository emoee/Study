# 시험환경 세팅 (코드 변경 X)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def exam_data_load(df, target, id_name="", null_name=""):
    if id_name == "":
        df = df.reset_index().rename(columns={"index": "id"})
        id_name = 'id'
    else:
        id_name = id_name
    
    if null_name != "":
        df[df == null_name] = np.nan
    
    X_train, X_test = train_test_split(df, test_size=0.2, random_state=2021)
    
    y_train = X_train[[id_name, target]]
    X_train = X_train.drop(columns=[target])

    
    y_test = X_test[[id_name, target]]
    X_test = X_test.drop(columns=[target])
    return X_train, X_test, y_train, y_test 
    
df = pd.read_csv("../input/pima-indians-diabetes-database/diabetes.csv")
X_train, X_test, y_train, y_test = exam_data_load(df, target='Outcome')

X_train.shape, X_test.shape, y_train.shape, y_test.shape

# 당뇨병 여부 판단
# 이상치 처리 (Glucose, BloodPressure, SkinThickness, Insulin, BMI가 0인 값)

# X_train.shape, X_test.shape, y_train.shape, y_test.shape
# print(X_train.info())
# print(X_test.info())
# print(y_train.info())

# print(len(X_train[X_train['Glucose'] == 0]))
# print(len(X_train[X_train['BloodPressure'] == 0]))
# print(len(X_train[X_train['SkinThickness'] == 0]))
# print(len(X_train[X_train['Insulin'] == 0]))
# print(len(X_train[X_train['BMI'] == 0]))

cols = ['Glucose','BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
cols_mean = X_train[cols].mean()
X_train[cols] = X_train[cols].replace(0, cols_mean)

cols_mean = X_test[cols].mean()
X_test[cols] = X_test[cols].replace(0, cols_mean)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
model_pred = model.predict(X_test)

result = pd.DataFrame({'idx': X_test.index, 'Outcome': model_pred[:, 1]})#.to_csv('1235.csv', index=False)
print(result)