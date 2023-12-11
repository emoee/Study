# Pclass, Gender, sibsp, parch를 독립변수로 사용하여 로지스틱 회귀모형을 실시하였을 때, 
# parch변수의 계수값은?

# (반올림하여 소수 셋째 자리까지 계산)
import pandas as pd

df = pd.read_csv("/kaggle/input/bigdatacertificationkr/Titanic.csv")
formula = "Survived ~ C(Pclass) + Gender + SibSp + Parch"

from statsmodels.formula.api import logit
model = logit(formula, data=df).fit()
print(model.params)

# C(Pclass): C()는 categorical 변수를 나타내며, 
# Pclass 변수를 각 클래스(1, 2, 3)로 나누어 모델에 포함시킵니다.

# 이러한 변수들이 종속 변수 Survived에 어떤 영향을 미치는지를 
# 통계적으로 분석하는 것이 로지스틱 회귀모형의 목적입니다. 

'''
Optimization terminated successfully.
         Current function value: 0.459565
         Iterations 6
Intercept         2.491729
C(Pclass)[T.2]   -0.848152
C(Pclass)[T.3]   -1.866905
Gender[T.male]   -2.760281
SibSp            -0.232553
Parch            -0.049847
dtype: float64
'''