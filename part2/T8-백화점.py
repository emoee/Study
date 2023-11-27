# 출력을 원하실 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

# 데이터 파일 읽기 예제
import pandas as pd
train = pd.read_csv("data/customer_train.csv")
test = pd.read_csv("data/customer_test.csv")

# print(train.info()) #결측치 : 환불금액, object: 주구매상품, 주구매지점
# print(test.info())

train = train.drop(columns = ['회원ID'])
train_sex = train.pop('성별')
test_id = test.pop('회원ID')

train['환불금액'] = train['환불금액'].fillna(0)
test['환불금액'] = test['환불금액'].fillna(0)

from sklearn.preprocessing import LabelEncoder
cols = ['주구매상품', '주구매지점']
for col in cols:
    le = LabelEncoder()
    train[col] = le.fit_transform(train[col])
    test[col] = le.transform(test[col])

# from sklearn.preprocessing import MinMaxScaler
# scaler = MinMaxScaler()
# col = ['환불금액', '총구매액', '최대구매액']
# train[col] = scaler.fit_transform(train[col])
# test[col] = scaler.transform(test[col])

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(train, train_sex, test_size = 0.2)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()#n_estimators = 100, max_depth = 5)
model.fit(xtrain, ytrain)
# model_pred = model.predict(xtest)

# from sklearn.metrics import roc_auc_score
# print(roc_auc_score(ytest, model_pred))

model_pred = model.predict(test)

result = pd.DataFrame({'pred' : model_pred})#.to_csv('result.csv', index = False)
print(result)

# 사용자 코딩

# 답안 제출 참고
# 아래 코드 예측변수 등은 개인별로 변경하여 활용
# pd.DataFrame변수.to_csv('result.csv', index=False)
