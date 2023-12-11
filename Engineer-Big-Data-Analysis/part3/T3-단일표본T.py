# 문제: 다음은 22명의 학생들이 국어시험에서 받은 점수이다. 학생들의 평균이 75보다 크다고 할 수 있는가?

# 귀무가설(H0): 모평균은 mu와 같다. (μ = mu), 학생들의 평균은 75이다
# 대립가설(H1): 모평균은 mu보다 크다. (μ > mu), 학생들의 평균은 75보다 크다

# 가정:
# 모집단은 정규분포를 따른다.
# 표본의 크기가 충분히 크다.
# 검정통계량, p-value, 검정결과를 출력하시오

# 데이터
scores = [75, 80, 68, 72, 77, 82, 81, 79, 70, 74, 76, 78, 81, 73, 81, 78, 75, 72, 74, 79, 78, 79]

from scipy import stats
mu = 75
s, p = stats.ttest_1samp(scores, mu, alternative='greater')
print('검정통계량 : ', round(s,4))
print('p-value : ', round(p,4))

result = 'f'
if (p>0.05):
    result = 't'

print(result)
# 검정통계량 :  1.7659
# p-value :  0.046
# f
# 결과가 f로 나왔다는 것은 p값이 유의수준보다 작은 것을 의미함, 즉 실험에 성공하였음, 대립가설 채택
# 즉 귀무가설은 기각됨