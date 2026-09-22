# %%
#Imports
import numpy as np
from scipy import stats

alpha = 0.05
print("Libraries imported and significance level set to alpha = 0.05")

# %%
# Question 1: One-Sample Z-Test Implementation

mu_0 = 50.0      # Claimed population mean (kg)
x_bar = 49.2     # Sample mean (kg)
sigma = 1.2      # Population standard deviation (kg)
n = 30           # Sample size

# Step 1: Z-statistic calculation
std_error = sigma / np.sqrt(n)
z_stat_1 = (x_bar - mu_0) / std_error

# Step 2: Two-tailed p-value calculation
p_val_1 = 2 * (1 - stats.norm.cdf(abs(z_stat_1)))

# Step 3: Reporting results
print("RESULTS FOR ONE-SAMPLE Z-TEST")
print(f"Null Hypothesis (H0): mu = {mu_0} kg")
print(f"Alternative Hypothesis (H1): mu != {mu_0} kg")
print(f"Significance Level (alpha): {alpha}")
print(f"Z-statistic: {z_stat_1:.4f}")
print(f"p-value: {p_val_1:.4f}")

# Step 4: Decision & Conclusion
if p_val_1 <= alpha:
    decision_1 = "Reject H0"
    conclusion_1 = (
        f"Since the p-value ({p_val_1:.4f}) <= alpha ({alpha}), we REJECT the null hypothesis. "
        f"There is sufficient statistical evidence that the average weight of Factory A's rice bags is significantly different from 50 kg."
    )
else:
    decision_1 = "Fail to Reject H0"
    conclusion_1 = (
        f"Since the p-value ({p_val_1:.4f}) > alpha ({alpha}), we FAIL TO REJECT the null hypothesis. "
        f"There is not enough statistical evidence to refute the company's claim that the average weight is 50 kg."
    )

print(f"Decision: {decision_1}")
print(f"Final Conclusion: {conclusion_1}")

# %%
# Question 2: Two-Sample Z-Test Implementation

# Given Data for Factory A
n_A = 30
x_bar_A = 49.5
sigma_A = 1.2

# Given Data for Factory B
n_B = 35
x_bar_B = 50.5
sigma_B = 1.4

# Step 1: Z-statistic calculation
pooled_std_error = np.sqrt((sigma_A**2 / n_A) + (sigma_B**2 / n_B))
z_stat_2 = (x_bar_A - x_bar_B) / pooled_std_error

# Step 2: Two-tailed p-value calculation
p_val_2 = 2 * (1 - stats.norm.cdf(abs(z_stat_2)))

# Step 3: Reporting results
print("RESULTS FOR TWO-SAMPLE Z-TEST")
print("Null Hypothesis (H0): mu_A - mu_B = 0 (No difference in average weights)")
print("Alternative Hypothesis (H1): mu_A - mu_B != 0 (Significant difference in average weights)")
print(f"Significance Level (alpha): {alpha}")
print(f"Z-statistic: {z_stat_2:.4f}")
print(f"p-value: {p_val_2:.4f}")

# Step 4: Decision & Conclusion
if p_val_2 <= alpha:
    decision_2 = "Reject H0"
    conclusion_2 = (
        f"Since the p-value ({p_val_2:.4f}) <= alpha ({alpha}), we REJECT the null hypothesis. "
        f"There is a statistically significant difference between the average weights of rice bags produced by Factory A and Factory B."
    )
else:
    decision_2 = "Fail to Reject H0"
    conclusion_2 = (
        f"Since the p-value ({p_val_2:.4f}) > alpha ({alpha}), we FAIL TO REJECT the null hypothesis. "
        f"There is no statistically significant difference between the average weights of rice bags from Factory A and Factory B."
    )

print(f"Decision: {decision_2}")
print(f"Final Conclusion: {conclusion_2}")