# 주어진 데이터는 고혈압 환자 치료 전후의 혈압이다. 
# 해당 치료가 효과가 있는지 대응(쌍체)표본 t-검정을 진행하시오

# (치료 후 혈압 - 치료 전 혈압)의 평균
# 유의수준: 0.05
# μ 의 표본평균은?(소수 둘째자리까지 반올림)
# 검정통계량 값은?(소수 넷째자리까지 반올림)
# p-값은?(소수 넷째자리까지 반올림)
# 가설검정의 결과는? (유의수준 5%)


# 치료의 효과가 있으면 혈압이 내려간다는 의미
# 즉, 대립가설은 혈압이 내려감
# 귀무가설은 그대로, 올라감
# 대립가설이 채택, 귀무가설은 기각 > 모든 기준은 귀무가설이 디폴트 값
import pandas as pd
data = pd.read_csv('part3/data/high_blood_pressure.csv')

result1 = round((data['bp_post'] - data['bp_pre']).mean(),2)

from scipy import stats
s , p = stats.ttest_rel(data['bp_post'], data['bp_pre'], alternative="less")
result2 = round(s, 4)
result3 = round(p, 4)

result4 = ''
if (p > 0.05): # p 값이 유의수준보다 좋으면 true, 즉 실험 실패, 대립가설은 기각, 귀무가설 채택
    result4 = 't'
else:
    result4 = 'f'
print(result1, result2, result3, result4)

# 여기서 result4가 f로 나왔으므로 p값이 유의수준보다 낮음을 의미
# 즉 실험에 성공하였으니 대립가설이 채택되었다는 의미, 즉 귀무가설은 기각되었음