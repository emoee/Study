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
    
df = pd.read_csv("기출문제/data/Train.csv.xls")
xtrain, xtest, ytrain, ytest = exam_data_load(df, target='Reached.on.Time_Y.N', id_name='ID')

# 전자상거래 배송 데이터

# 제품 배송 시간에 맞춰 배송되었는지 예측모델 만들기

# 학습용 데이터 (X_train, y_train)을 이용하여 배송 예측 모형을 만든 후, 
# 이를 평가용 데이터(X_test)에 적용하여 얻은 예측 확률값을 다음과 같은 형식의 CSV파일로 생성하시오
# (제출한 모델의 성능은 ROC-AUC 평가지표에 따라 채점)

# ID, Reached.on.Time_Y.N
# 4733,0.6
# 2040,0.8
# 5114,0.45
# 2361,0.23
# 5996,0.43
# [시험용 데이터셋 만들기] 코드는 예시문제와 동일한 형태의 X_train, y_train, X_test 데이터를 만들기 위함임

# (유의사항)

# 성능이 우수한 예측모형을 구축하기 위해서는 적절한 데이터 전처리, 피처엔지니어링, 분류알고리즘, 하이퍼파라미터 튜닝, 모형 앙상블 등이 수반되어야 한다.
# 수험번호.csv파일이 만들어지도록 코드를 제출한다.
# 제출한 모델의 성능은 ROC-AUC형태로 읽어드린다.

# print(xtrain.info()) # object : Warehouse_block, Mode_of_Shipment, Product_importance, Gender
# print(xtest.info())
# print(ytrain.info())

# print(xtrain['Gender'].unique())
# print(xtest['Gender'].unique())
# label : Warehouse_block, Mode_of_Shipment,Product_importance

xtest_id = xtest.pop('ID')
xtrain = xtrain.drop(columns = ['ID'])

xtrain = pd.get_dummies(data = xtrain, columns=['Gender'])
xtest = pd.get_dummies(data = xtest, columns=['Gender'])

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
xtrain['Warehouse_block'] = encoder.fit_transform(xtrain['Warehouse_block'])
xtest['Warehouse_block'] = encoder.transform(xtest['Warehouse_block'])

xtrain['Mode_of_Shipment'] = encoder.fit_transform(xtrain['Mode_of_Shipment'])
xtest['Mode_of_Shipment'] = encoder.transform(xtest['Mode_of_Shipment'])

xtrain['Product_importance'] = encoder.fit_transform(xtrain['Product_importance'])
xtest['Product_importance'] = encoder.transform(xtest['Product_importance'])

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(xtrain, ytrain['Reached.on.Time_Y.N'])
model_pred = model.predict_proba(xtest)

from sklearn.metrics import roc_auc_score
print(roc_auc_score(ytest['Reached.on.Time_Y.N'],model_pred[:,1]))

result = pd.DataFrame({'ID' : xtest_id, 'Reached.on.Time_Y.N' : model_pred[:,1]})#.to_csv('result.csv', index = False)
print(result)