import pandas as pd

train = pd.read_csv("../input/big-data-analytics-certification-kr-2022/train.csv")
test = pd.read_csv("../input/big-data-analytics-certification-kr-2022/test.csv")

# 데이터 파악
# print(train.info()) # 삭제 : ID / pop : Segmentation  
# print(test.info()) # pop : ID 

train = train.drop(columns = ['ID'])
train_seg = train.pop('Segmentation')
test_id = test.pop('ID')

# object : Gender /  Ever_Married /Graduated   /Profession /Spending_Score /Var_1 
# 원핫인코딩 : Gender, Ever_Married, Graduated, Spending_Score
# 라벨인코딩 : Profession, Var_1

col = ['Gender', 'Ever_Married', 'Graduated', 'Spending_Score']
train = pd.get_dummies(data=train, columns=col)
test = pd.get_dummies(data=test, columns=col)

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
train['Profession'] = encoder.fit_transform(train['Profession'])
test['Profession'] = encoder.transform(test['Profession'])

train['Var_1'] = encoder.fit_transform(train['Var_1'])
test['Var_1'] = encoder.transform(test['Var_1'])

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(train, train_seg, test_size = 0.2)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(xtrain, ytrain)
model_pred = model.predict(test)

result = pd.DataFrame({'ID': test_id, 'Segmentation': model_pred}).to_csv('submission.csv', index = False)
print(result)