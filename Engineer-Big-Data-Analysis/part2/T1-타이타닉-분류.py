# 생존여부 예측모델 만들기
# 학습용 데이터 (X_train, y_train)을 이용하여 생존 예측 모형을 만든 후, 
# 이를 평가용 데이터(X_test)에 적용하여 얻은 예측값을 다음과 같은 형식의 CSV파일로 생성하시오
# (제출한 모델의 성능은 accuracy 평가지표에 따라 채점)

# (가) 제공 데이터 목록
# y_train: 생존여부(학습용)
# X_trian, X_test : 승객 정보 (학습용 및 평가용)

# (나) 데이터 형식 및 내용
# y_trian (712명 데이터)
# 시험환경 세팅은 예시문제와 동일한 형태의 X_train, y_train, X_test 데이터를 만들기 위함임

# 유의사항
# 성능이 우수한 예측모형을 구축하기 위해서는 적절한 데이터 전처리, 피처엔지니어링, 분류알고리즘, 하이퍼파라미터 튜닝, 모형 앙상블 등이 수반되어야 한다.
# 수험번호.csv파일이 만들어지도록 코드를 제출한다.
# 제출한 모델의 성능은 accuracy로 평가함

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
    
df = pd.read_csv("../input/titanic/train.csv")
X_train, X_test, y_train, y_test = exam_data_load(df, target='Survived', id_name='PassengerId')

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

print(X_train.info())
print(X_train.head())

X_train = X_train.drop(columns = ['Age'])
X_test = X_test.drop(columns = ['Age'])

X_train = X_train.drop(columns = ['Embarked'])
X_test = X_test.drop(columns = ['Embarked'])

X_train = X_train.drop(columns = ['Cabin'])
X_test = X_test.drop(columns = ['Cabin'])

X_train = X_train.drop(columns = ['Name'])
X_test = X_test.drop(columns = ['Name'])

X_train = pd.get_dummies(X_train, columns=['Sex'], drop_first=True) # 원 핫 인코딩
X_test = pd.get_dummies(X_test, columns=['Sex'], drop_first=True)

X_train = X_train.drop(columns = ['Ticket'])
X_test = X_test.drop(columns = ['Ticket'])

print(X_train.info())
print(X_train.head())

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
model_pred = model.predict(X_test)
# print(model_pred)

pred = model_pred[:, 1]
# print(pred_id, pred)

pd.DataFrame({'PassengerId': X_test.PassengerId, 'Survived': pred}).to_csv('1234.csv', index=False)