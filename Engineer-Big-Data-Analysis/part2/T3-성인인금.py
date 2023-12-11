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
    
df = pd.read_csv("../input/adult-census-income/adult.csv")
x_train, x_test, y_train, y_test = exam_data_load(df, target='income', null_name='?')

#X_train.shape, X_test.shape, y_train.shape, y_test.shape

'''
성인 인구조사 소득 예측

age: 나이
workclass: 고용 형태
fnlwgt: 사람의 대표성을 나타내는 가중치(final weight)
education: 교육 수준
education.num: 교육 수준 수치
marital.status: 결혼 상태
occupation: 업종
relationship: 가족 관계
race: 인종
sex: 성별
capital.gain: 양도 소득
capital.loss: 양도 손실
hours.per.week: 주당 근무 시간
native.country: 국적
income: 수익 (예측해야 하는 값)
'''
#print(x_train.info()) # 삭제 : id, 결측치 : workclass, occupation, native, 
# object : workclass, education, education.num,marital.status, occupation,relationship, race, sex, native.country

#print(y_train.info()) # 삭제 : id, object : income

#print(x_test.info()) # 삭제 : id, 결측치 : workclass, occupation, native
# object : workclass, education,marital.status, occupation,relationship, race, sex, native.country

#print(y_train.head())
'''
          id income
21851  21851   >50K
7632    7632  <=50K
27878  27878  <=50K
14121  14121  <=50K
32345  32345  <=50K
'''

# 데이터 삭제
x_train = x_train.drop(columns=['id','education'])
x_test = x_test.drop(columns=['education'])
x_test_id = x_test.pop('id')
y_train = y_train.drop(columns=['id'])

# 결측치 처리 : workclass, occupation, native.country : 여기서는 최빈값으로 처리하면 됨
# print(x_train['Private'].value_counts()) 
# workclass = Private / occupation = Exec-managerial / native.country : United-States
x_train['workclass'] = x_train['workclass'].fillna('Private')
x_test['workclass'] = x_test['workclass'].fillna('Private')

x_train['occupation'] = x_train['occupation'].fillna('Exec-manageria')
x_test['occupation'] = x_test['occupation'].fillna('Exec-manageria')

x_train['native.country'] = x_train['native.country'].fillna('United-States')
x_test['native.country'] = x_test['native.country'].fillna('United-States')

# object 처리 
# x_train = object : workclass, education, marital.status, occupation,relationship, race, sex, native.country
# x_test = object : workclass, education,marital.status, occupation,relationship, race, sex, native.country

# 원핫인코딩 : sex/ 라벨인코딩 : 'workclass' -8, 'education'-16 , 'marital.status', occupation, relationship, race, native.country
# print(x_train['education.num'].unique())

# 원핫인코딩
x_train = pd.get_dummies(x_train, columns = ['sex'])
x_test = pd.get_dummies(x_test, columns = ['sex'])

# 라벨인코딩
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
# 'workclass','marital.status','occupation','relationship','race','native.country']
x_train['workclass'] = encoder.fit_transform(x_train['workclass'])
x_test['workclass'] = encoder.fit_transform(x_test['workclass'])

x_train['marital.status'] = encoder.fit_transform(x_train['marital.status'])
x_test['marital.status'] = encoder.fit_transform(x_test['marital.status'])

x_train['occupation'] = encoder.fit_transform(x_train['occupation'])
x_test['occupation'] = encoder.fit_transform(x_test['occupation'])

x_train['relationship'] = encoder.fit_transform(x_train['relationship'])
x_test['relationship'] = encoder.fit_transform(x_test['relationship'])

x_train['native.country'] = encoder.fit_transform(x_train['native.country'])
x_test['native.country'] = encoder.fit_transform(x_test['native.country'])

x_train['race'] = encoder.fit_transform(x_train['race'])
x_test['race'] = encoder.fit_transform(x_test['race'])

# 데이터 스케링일
ncol = ['age','fnlwgt', 'education.num','capital.gain','capital.loss','hours.per.week']
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
x_train[ncol] = scaler.fit_transform(x_train[ncol]) 
x_test[ncol] = scaler.fit_transform(x_test[ncol])

# income 데이터 변경
y_train = (y_train['income'] == '>50K').astype(int)

# 데이터 학습
# from sklearn.model_selection import train_test_split
# x_train1, x_test1, y_train1, y_test1 = train_test_split(x_train, y_train, test_size = 0.2)

# from sklearn.ensemble import RandomForestClassifier
# model2 = RandomForestClassifier(n_estimators=50, max_depth= 15)
# model2.fit(x_train1, y_train1)
# model_pred2 = model2.predict(x_test1)

# from sklearn.metrics import accuracy_score
# print(accuracy_score(y_test1, model_pred2))
# print('=====')

# 찾은 하이퍼파리미터 값으로 제출
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=50, max_depth= 15)
model.fit(x_train, y_train)
model_pred = model.predict(x_test)

result = pd.DataFrame({'id': x_test_id, 'income':model_pred})#.to_csv('123.csv', index=False)
print(result)
