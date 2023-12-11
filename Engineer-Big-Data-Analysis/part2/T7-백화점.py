# # 아래는 백화점 고객의 1년 간 구매 데이터이다.
# (가) 제공 데이터 목록
# 1 y_train.csv : 고객의 성별 데이터 (학습용), CSV 형식의 파일
# 2 X_train.csv, X_test.csv : 고객의 상품구매 속성 (학습용 및 평가용), CSV 형식의 파일

# (나) 데이터 형식 및 내용
# 1 y_train.csv (3,500명 데이터)
# * custid: 고객 ID
# * gender: 고객의 성별 (0: 여자, 1: 남자)
# 2 X_train.csv (3,500명 데이터), X_test.csv (2,482명 데이터)

# 고객 3,500명에 대한 학습용 데이터(y_train.csv, X_train.csv)를 이용하여 성별예측 모형을 만든 후, 
# 이를 평가용 데이터(X_test.csv)에 적용하여 얻은 2,482명 고객의 성별 예측값(남자일 확률)을 
# 다음과 같은 형식의 CSV 파일로 생성하시오.(제출한 모델의 성능은 ROC-AUC 평가지표에 따라 채점)

# <유의사항>
# 성능이 우수한 예측모형을 구축하기 위해서는 
# 적절한 데이터 전처리, Feature Engineering, 분류 알고리즘 사용, 초매개변수 최적화, 모형 앙상블 등이 
# 수반되어야 한다.
# custid,gender 3500,0.267 3501,0.578 3502,0.885 ...

import pandas as pd
# 데이터 불러오기
x_train = pd.read_csv("part2/data/X_train.csv", encoding="euc-kr") # 구름 IDE환경에서는 encoding="euc-kr"가 없어도 됨
y_train = pd.read_csv("part2/data/y_train.csv")
x_test = pd.read_csv("part2/data/X_test.csv", encoding="euc-kr")

# 모형 : 분류 RandomForestClassifier
# 데이터 확인
# print(x_train.info()) # 불필요 컬럼 : cust_id/ 결측치 : 환불금액/ object : 주구매상품, 주구매지점
# print(x_test.info()) # 불필요 컬럼 : cust_id/ 결측치 : 환불금액/ object : 주구매상품, 주구매지점
# print(y_train.info()) # 불필요 컬럼 : cust_id

x_train = x_train.drop(columns=['cust_id'])
x_test_id = x_test.pop('cust_id')
y_train = y_train.drop(columns=['cust_id'])

# print(x_test['환불금액'].describe())
# print(x_train['환불금액'].median())
# print(x_train['환불금액'].mean())

# 결측치
x_train['환불금액'] = x_train['환불금액'].fillna(x_train['환불금액'].mean())
x_test['환불금액'] = x_test['환불금액'].fillna(x_test['환불금액'].mean())

# object
# x_train['주구매상품'].unique()
# x_train['주구매지점'].unique()
# x_train['주구매상품'].value_count()
# x_train['주구매지점'].value_count()

# 라벨인코딩
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
x_train['주구매상품'] = encoder.fit_transform(x_train['주구매상품'])
x_test['주구매상품'] = encoder.transform(x_test['주구매상품'])

x_train['주구매지점'] = encoder.fit_transform(x_train['주구매지점'])
x_test['주구매지점'] = encoder.transform(x_test['주구매지점'])

# 스케일링
from sklearn.preprocessing import RobustScaler
scol = ['총구매액','최대구매액', '내점일수','내점당구매건수','주말방문비율','구매주기']
scaler = RobustScaler()
x_train[scol] = scaler.fit_transform(x_train[scol])
x_test[scol] = scaler.transform(x_test[scol])

# 데이터 찢기
# from sklearn.model_selection import train_test_split
# x_train1, x_test1, y_train1, y_test1 = train_test_split(x_train, y_train, test_size = 0.2)

# 최적의 하이퍼파라미터 찾기
# from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier(n_estimators=140, max_depth=18)
# model.fit(x_train1, y_train1)
# model_pred = model.predict_proba(x_test1)

# from sklearn.metrics import roc_auc_score
# print(roc_auc_score(y_test1, model_pred[:,1]))

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, max_depth=7)
model.fit(x_train, y_train)
model_pred = model.predict_proba(x_test)

# print(model_pred)
pred = model_pred[:, 1]

result = pd.DataFrame({'custid' : x_test_id, 'gender' :pred})#.to_csv('12.csv', index=False)
print(result)