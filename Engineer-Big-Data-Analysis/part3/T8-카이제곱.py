from scipy.stats import chisquare

observed_frequencies = [30, 60, 50, 40, 20]
expected_frequencies = [200 * 0.20, 200 * 0.30, 200 * 0.25, 200 * 0.15, 200 * 0.10]

s, p = chisquare(f_obs=observed_frequencies, f_exp=expected_frequencies)
print(s, p)
result = 'f'
if (p>0.05):
    result = 't'
print(result)
# 5.833333333333334 0.21194558437271782 t
# 결과가 t이므로 실험에 실패, 즉 귀무가설을 채택한다. 