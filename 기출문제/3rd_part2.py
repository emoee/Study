# 여행 보험 패키지 상품을 구매할 확률 값을 구하시오

# 예측할 값(y): TravelInsurance (여행보험 패지지를 구매 했는지 여부 0:구매안함, 1:구매)
# 평가: roc-auc 평가지표
# data: t2-1-train.csv, t2-1-test.csv
# 제출 형식
# id,TravelInsurance
# 0,0.3
# 1,0.48
# 2,0.3
# 3,0.83

import pandas as pd

train = pd.read_csv("../input/big-data-analytics-certification/t2-1-train.csv")
test = pd.read_csv("../input/big-data-analytics-certification/t2-1-test.csv")

# 데이터 파악
# print(train.info()) # 결측치 : AnnualIncome / object : Employment Type  GraduateOrNot  FrequentFlyer EverTravelledAbroad
# print(test.info())

train = train.drop(columns=['id'])
train_travel = train.pop('TravelInsurance')
test_id = test.pop('id')

train['AnnualIncome'] = train['AnnualIncome'].fillna(train['AnnualIncome'].min())
test['AnnualIncome'] = test['AnnualIncome'].fillna(test['AnnualIncome'].min())

# print(train['EverTravelledAbroad'].unique())
# 원핫인코딩 : Employment Type, GraduateOrNot, FrequentFlyer, EverTravelledAbroad
col = ['GraduateOrNot', 'FrequentFlyer', 'EverTravelledAbroad']
train = pd.get_dummies(data = train, columns = col)
test = pd.get_dummies(data = test, columns = col)

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
train['Employment Type'] = encoder.fit_transform(train['Employment Type'])
test['Employment Type'] = encoder.fit_transform(test['Employment Type'])

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(train, train_travel, test_size = 0.2)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(xtrain, ytrain)
model_pred = model.predict_proba(test)
pred = model_pred[:,1]

# from sklearn.metrics import roc_auc_score
# print(roc_auc_score(ytest, pred))

result = pd.DataFrame({'id' : test_id, 'TravelInsurance' : pred}).to_csv("2022.csv",index=False)
print(result)