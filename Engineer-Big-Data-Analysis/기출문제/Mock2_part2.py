# 대학원 입학 예측(회귀)

# 예측할 값(target): "Chance of Admit "
# 평가: r2
# data(3개): t2-2-X_train, t2-2-y_train, t2-2-X_test
# 제출 형식(Serial No.-> id, 예측 값 -> target)
# id,target
# 28,0.741696
# 76,0.779616
# 151,0.897247

# 라이브러리 불러오기
import pandas as pd

xtrain = pd.read_csv("../input/big-data-analytics-certification/t2-2-X_train.csv")
ytrain = pd.read_csv("../input/big-data-analytics-certification/t2-2-y_train.csv")
xtest = pd.read_csv("../input/big-data-analytics-certification/t2-2-X_test.csv")

# print(xtrain.info())
# print(ytrain.info())
# print(xtest.info())

xtest_no = xtest.pop('Serial No.')
xtrain = xtrain.drop(columns = ['Serial No.'])

# print(xtrain.describe())
# print(xtest.describe())
# print(ytrain.head())

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
col = ['GRE Score','TOEFL Score']
xtrain[col] = scaler.fit_transform(xtrain[col])
xtest[col] = scaler.transform(xtest[col])

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(xtrain, ytrain)
model_pred = model.predict(xtest)
pred = model_pred[:,1]

# from sklearn.model_selection import cross_val_score
# scores = cross_val_score(rf, X_train.iloc[:,1:] , y_train["Chance of Admit "] , scoring='r2', cv=5)
# print(scores.mean())

result = pd.DataFrame({'id': xtest_no, 'target': pred}).to_csv('result.csv', index = False)
print(result)
