# %%
#Import libraries
import numpy as np
from scipy import stats

# %%
#Given data
population_mean = 50
population_std = 1.2
sample_size = 30
sample_mean = 49.2
alpha = 0.05

# %%
#Null and alternate hypothesis
print("Null Hypothesis (H₀): μ = 50 kg")
print("Alternative Hypothesis (H₁): μ ≠ 50 kg")

# %%
#Perform z test
z_stat = (sample_mean - population_mean) / (
    population_std / np.sqrt(sample_size)
)

print("Z-statistic:", z_stat)

p_value = 2 * stats.norm.sf(abs(z_stat))

print("P-value:", p_value)

if p_value < alpha:
    print("Decision: Reject H₀")
else:
    print("Decision: Fail to Reject H₀")

if p_value < alpha:
    print("Conclusion: There is sufficient evidence to reject the company's claim.")
    print("The average weight of the rice bags is significantly different from 50 kg.")
else:
    print("Conclusion: There is not sufficient evidence to reject the company's claim.")
    print("The average weight of the rice bags is not significantly different from 50 kg.")