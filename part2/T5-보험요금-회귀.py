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
    
df = pd.read_csv("../input/insurance/insurance.csv")
x_train, x_test, y_train, y_test = exam_data_load(df, target='charges')

# 보험 요금??? 회귀 모델 RandomForestRegressor
# Insurance Prediction (Regression)
# 오늘 저희는 의료보험 데이터를 활용해 한 사람이 보험료를 얼마나 낼지를 예측하는 회귀 문제를 다뤄보겠습니다. 
# 위의 input에 추가된 데이터에서 바로 이용할 수 있고, 데이터를 이루고 있는 column들에 대한 설명은 다음과 같습니다.

# Age: 피보험자의 나이
# Sex: 피보험자의 성별
# BMI: 피보험자의 체질량 지수

# Children: 피보험자의 자녀의 수
# Smoker: 흡연 여부 (yes / no)
# Region: 피보험자가 거주하는 지역 (Southeast / Southwest / Northeast / Northwest)
# Charges: 보험료

# print(x_train.info()) # 불필요컬럼 : 결측치 : 없음 / object : sex, smoker, region
# print(x_test.info()) # 결측치 : 없음 / object : sex, smoker, region
# print(y_train.info())

# print(x_train.isnull().sum())
# print(x_test.isnull().sum())
# print(y_train.isnull().sum())

# 삭제
x_train = x_train.drop(columns=['id'])
x_test_id = x_test.pop('id')
y_train = y_train.drop(columns=['id'])


# 원핫 인코딩 : sex, smoker / 라벨 : region
ocol = ['sex', 'smoker']
x_train = pd.get_dummies(data = x_train, columns = ocol)
x_test = pd.get_dummies(data = x_test, columns = ocol)

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
x_train['region'] = encoder.fit_transform(x_train['region'])
x_test['region'] = encoder.transform(x_test['region'])

# 스케일링
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
rcol = ['age', 'bmi']
x_train[rcol] = scaler.fit_transform(x_train[rcol])
x_test[rcol] = scaler.transform(x_test[rcol])

# 데이터 찢기
# from sklearn.model_selection import train_test_split
# x_train1, x_test1, y_train1, y_test1 = train_test_split(x_train, y_train, test_size = 0.2)

# from sklearn.ensemble import RandomForestRegressor
# model3 = RandomForestRegressor(n_estimators = 100, max_depth=5)
# model3.fit(x_train1, np.ravel(y_train1))
# model_pred3 = model3.predict(x_test1)

# from sklearn.metrics import mean_squared_error
# rmse2 = np.sqrt(mean_squared_error(y_test1, model_pred3))
# print("Mean Squared Error:", rmse2)

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators = 100, max_depth=5)
model.fit(x_train, np.ravel(y_train))
model_pred = model.predict(x_test)

result = pd.DataFrame({'id': x_test_id , 'charges':model_pred})#.to_csv('123.csv', index=False)
print(result)

rmse(y_test['charges'], model_pred)
