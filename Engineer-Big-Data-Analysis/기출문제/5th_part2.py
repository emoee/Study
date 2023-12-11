# 빅데이터 분석기사 5회 실기 기출 유형

# [가격 예측] 중고 자동차
# 자동차 가격을 예측해주세요!
# 예측할 값(y): price
# 평가: RMSE (Root Mean Squared Error)
# data: train.csv, test.csv
# [컴피티션 제출 양식] 리더보드 제출용

# 제출 형식: submission.csv파일을 아래와 같은 형식(수치형)으로 제출
# (id는 test의 index임)
# id,price
# 0,11000
# 1,20500
# 2,19610
# ...    
# 1616,11995

import pandas as pd
# 데이터 로드
train = pd.read_csv("/kaggle/input/big-data-analytics-certification-kr-2023-5th/train.csv")
test = pd.read_csv("/kaggle/input/big-data-analytics-certification-kr-2023-5th/test.csv")
submission = pd.read_csv("/kaggle/input/big-data-analytics-certification-kr-2023-5th/sample_submission.csv")
submission = submission.pop('id')

# print(train.info()) # object : model, transmission, fuelType
# print(test.info())

train_price = train.pop('price')

# print(test['transmission'].unique())

# Label : model
# one-hot : transmission, fuelType

col = ['transmission', 'fuelType']
train = pd.get_dummies(data= train, columns = col)
test = pd.get_dummies(data= test, columns = col)

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
train['model'] = encoder.fit_transform(train['model'])
test['model'] = encoder.transform(test['model'])

from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
rcol = ['mileage', 'tax']
train[rcol] = scaler.fit_transform(train[rcol])
test[rcol] = scaler.transform(test[rcol])

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(train, train_price, test_size = 0.2)

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(xtrain, ytrain)
model_pred = model.predict(test)

result = pd.DataFrame({'id':submission, 'price' : model_pred}).to_csv('submission.csv', index=False)
print(result)
# import sklearn.metrics
# print(rmse(ytest, model_pred))