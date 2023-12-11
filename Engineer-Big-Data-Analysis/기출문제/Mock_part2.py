################## 시험 안내 문구 및 코드 ##################
# 출력을 원하실 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

# 데이터 파일 읽기 예제
import pandas as pd
xtest = pd.read_csv("../input/hr-data/X_test.csv")
xtrain = pd.read_csv("../input/hr-data/X_train.csv")
ytrain = pd.read_csv("../input/hr-data/y_train.csv")

# 사용자 코딩

# 답안 제출 참고
# 아래 코드 예측변수와 수험번호를 개인별로 변경하여 활용
# pd.DataFrame({'enrollee_id': X_test.enrollee_id, 'target': pred}).to_csv('003000000.csv', index=False)

# 모의고사

# 이진 분류
# 이직할 사람을 찾는 문제(확률)
# 평가

# 확률값 예측
# roc-auc
# target

# 0: 이직할 마음 없음
# 1: 이직할 회사 찾음

# print(xtrain.info())
# print(xtest.info())
# print(ytrain.info())

xtrain = xtrain.drop(columns= ['city', 'enrollee_id', 'company_size', 'company_type'])
xtest = xtest.drop(columns= ['city','company_size', 'company_type'])
xtest_id = xtest.pop('enrollee_id')

# print(xtest['gender'].mode()) # Male
# print(xtrain['enrolled_university'].mode()) # no_enrollment 
# print(xtrain['education_level'].mode()) # Graduate
# print(xtrain['major_discipline'].mode()) # STEM
# print(xtrain['experience'].mode()) # >20
# print(xtrain['last_new_job'].mode()) # 1

# 결측치 처리 : gender  , enrolled_university, education_level ,major_discipline ,experience,last_new_job  
# 학습데이터와 테스트 데이터 mode값 일치함
xtrain['gender'] = xtrain['gender'].fillna('Male')
xtest['gender'] = xtest['gender'].fillna('Male')

xtrain['enrolled_university'] = xtrain['enrolled_university'].fillna('no_enrollment')
xtest['enrolled_university'] = xtest['enrolled_university'].fillna('no_enrollment')

xtrain['education_level'] = xtrain['education_level'].fillna('Graduate')
xtest['education_level'] = xtest['education_level'].fillna('Graduate')

xtrain['major_discipline'] = xtrain['major_discipline'].fillna('STEM')
xtest['major_discipline'] = xtest['major_discipline'].fillna('STEM')

xtrain['experience'] = xtrain['experience'].fillna('>20')
xtest['experience'] = xtest['experience'].fillna('>20')

xtrain['last_new_job'] = xtrain['last_new_job'].fillna('1')
xtest['last_new_job'] = xtest['last_new_job'].fillna('1')

# object 처리  major_discipline,experience,last_new_job 
# 원핫 : 'relevent_experience', 'gender'
# 라벨 : 'enrolled_university', 'education_level', major_discipline,experience,last_new_job 

xtrain = pd.get_dummies(data = xtrain, columns = ['relevent_experience', 'gender'])
xtest = pd.get_dummies(data = xtest, columns = ['relevent_experience', 'gender'])

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
columns = ['enrolled_university', 'education_level', 'major_discipline', 'experience', 'last_new_job']
for column in columns:
    xtrain[column] = encoder.fit_transform(xtrain[column])
    xtest[column] = encoder.transform(xtest[column])

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators = 50, max_depth = 8)
model.fit(xtrain, ytrain['target'])
model_pred = model.predict(xtest)

result = pd.DataFrame({'enrollee_id' : xtest_id, 'target' : model_pred})#.to_csv('result.csv', index=False)
print(result)

# from sklearn.metrics import roc_auc_score
# import pickle
# with open( "../input/hr-data/answer.pickle", "rb" ) as file:
#     ans = pickle.load(file)
#     ans = pd.DataFrame(ans)
# print(roc_auc_score(ans['target'], model_pred))