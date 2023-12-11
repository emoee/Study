'''
왜도와 첨도 구하기

주어진 데이터 중 train.csv에서 'SalePrice'컬럼의 왜도와 첨도를 구한 값과, 'SalePrice'컬럼을 스케일링(log1p)로 변환한 이후 왜도와 첨도를 구해 모두 더한 다음 소수점 2째자리까지 출력하시오
데이터셋 : House Prices - Advanced Regression Technique (https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
오른쪽 상단 copy&edit 클릭 -> 예상문제 풀이 시작
강의 영상 : https://youtu.be/_ft7ZlDlk7c

왜도 : 비대칭도(非對稱度, skewness) 또는 왜도(歪度)는 실수 값 확률 변수의 확률 분포 비대칭성을 나타내는 지표이다. 
왜도가 양수일 때는 확률밀도함수의 오른쪽 부분에 긴 꼬리를 가지며 자료가 왼쪽에 더 많이 분포해 있다는 것을 나타낸다. 
평균과 중앙값이 같으면 왜도는 0이 된다.

첨도 : 확률분포의 꼬리가 두꺼운 정도를 나타내는 척도이다. 극단적인 편차 또는 이상치가 많을 수록 큰 값을 나타낸다. 
첨도값(K)이 3에 가까우면 산포도가 정규분포에 가깝다. 3보다 작을 경우에는(K<3) 산포는 정규분포보다 꼬리가 얇은 분포로 생각할 수 있다, 
첨도값이 3보다 큰 양수이면(K>3) 정규분포보다 꼬리가 두꺼운 분포로 판단할 수 있다.

'''
import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/house-prices-advanced-regression-techniques/train.csv')
spskew = df['SalePrice'].skew() # DataFrame.skew() 왜도
spkurt = df['SalePrice'].kurt() # DataFrame.kurt() 첨도

df['SalePrice'] = np.log1p(df['SalePrice'])
spskew2 = df['SalePrice'].skew() # DataFrame.skew() 왜도
spkurt2 = df['SalePrice'].kurt() # DataFrame.kurt() 첨도

print(round(spskew + spkurt + spskew2 + spkurt2, 2))

# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/house-prices-advanced-regression-techniques/train.csv')
df.head(5)
df['SalePrice'].hist()

# 'SalePrice'컬럼 왜도와 첨도계산
s1 = df['SalePrice'].skew() # DataFrame.skew() 왜도
k1 = df['SalePrice'].kurt() # DataFrame.kurt() 첨도
print("왜도:" ,s1)
print("첨도:" ,k1)
df['SalePrice'].hist()

# 'SalePrice'컬럼 로그변환
df['SalePrice'] = np.log1p(df['SalePrice'])

# 'SalePrice'컬럼 왜도와 첨도계산 
s2 = df['SalePrice'].skew() # DataFrame.skew() 왜도
k2 = df['SalePrice'].kurt() # DataFrame.kurt() 첨도
print("왜도:" ,s2)
print("첨도:" ,k2)
df['SalePrice'].hist()

# 모두 더한 다음 출력
print(s1+s2+k1+k2)
print(round(s1+s2+k1+k2,2))

# 정답 9.35