# 자전거 수요 예측

import pandas as pd
train = pd.read_csv("/kaggle/input/bike-sharing-demand/train.csv")
test = pd.read_csv("/kaggle/input/bike-sharing-demand/test.csv")

# print(train.info()) # 불필요 데이터 : casual,registered,count  # 결측치 : 없음 # object :  datetime
# print(test.info()) # object :  datetime

# 삭제
train = train.drop(columns = ['casual', 'registered'])
target = train.pop('count')

# object
train['datetime'] = pd.to_datetime(train['datetime'])
test['datetime'] = pd.to_datetime(test['datetime'])

train['year'] = train['datetime'].dt.year
train['month'] = train['datetime'].dt.month
train['day'] = train['datetime'].dt.day

test['year'] = test['datetime'].dt.year
test['month'] = test['datetime'].dt.month
test['day'] = test['datetime'].dt.day

train = train.drop(columns=['datetime'])
test_datetime = test.pop('datetime')

# 스케일링
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
rcol = ['temp', 'atemp', 'humidity']
train[rcol] = scaler.fit_transform(train[rcol])
test[rcol] = scaler.transform(test[rcol])

# 데이터 분할
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(train, target, test_size=0.2)


from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators = 140, max_depth=13)
model.fit(x_train,y_train)
model_pred = model.predict(test)

# from sklearn.metrics import r2_score
# print(r2_score(y_test, model_pred))

result = pd.DataFrame({'datetime': test_datetime, 'count': model_pred})#.to_csv('123.csv',index=False)
print(result)
print(result.shape, test.shape)