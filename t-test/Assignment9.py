# %%
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# %%
#One-sample t-test

#Dataset 1
energy_weights = [
    49.5, 50.2, 48.7, 51.1, 49.9,
    50.5, 49.8, 50.3, 49.7, 50.6,
    50.1, 49.4, 50.0, 49.6, 50.8,
    49.3, 50.4, 50.7, 49.2, 50.9
]

# %%
#Null hypothesis and alternate hypothesis
print("NUll hypothesis: mean is 50 grams")

print("Alternate hypothesis: mean is not equal to 50 grams")

print("Significance level: 0.05")

# %%
#Check normality of the dataset using visualization (histogram/QQ plot).
plt.figure(figsize=(9, 5))

plt.hist(
    energy_weights,
    bins=np.arange(48.5, 51.6, 0.5),
    edgecolor='black',
    linewidth=1.2
)

# Add the claimed mean
plt.axvline(
    50,
    linestyle='--',
    linewidth=2,
    label='Claimed Mean = 50 g'
)

plt.xlabel("Weight (grams)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.title("Distribution of Energy Bar Weights", fontsize=15)

plt.xticks(np.arange(48.5, 51.6, 0.5))
plt.grid(axis='y', linestyle=':', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()

# %%
#Perform one sample t-test
t_stat, p_value = stats.ttest_1samp(energy_weights, 50)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")


# %%
#Two-sample t-test
#Dataset 2
method_A = [78, 85, 82, 90, 76, 88, 84, 79, 91, 77]

method_B = [72, 81, 79, 74, 69, 83, 78, 75, 80, 71]

# %%
#Null hypothesis and alternate hypothesis
print("NUll hypothesis:There is no significant difference between the average scores.")

print("Alternate hypothesis: There is a significant difference between the average scores.")

print("Significance level: 0.05")

# %%
#Check normality of the dataset using visualization (histogram/QQ plot).
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(9, 5))

plt.hist(
    method_A,
    bins=np.arange(74.5, 92.5, 3),
    edgecolor='black',
    linewidth=1.2
)

# Mean line
mean_A = np.mean(method_A)

plt.axvline(
    mean_A,
    linestyle='--',
    linewidth=2,
    label=f'Mean = {mean_A:.1f}'
)

plt.xlabel("Scores", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.title("Distribution of Scores - Method A", fontsize=15)

plt.xticks(np.arange(75, 93, 2))
plt.grid(axis='y', linestyle=':', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))

plt.hist(
    method_B,
    bins=np.arange(68.5, 84.5, 3),
    edgecolor='black',
    linewidth=1.2
)

mean_B = np.mean(method_B)

plt.axvline(
    mean_B,
    linestyle='--',
    linewidth=2,
    label=f'Mean = {mean_B:.1f}'
)

plt.xlabel("Scores", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.title("Distribution of Scores - Method B", fontsize=15)

plt.xticks(np.arange(69, 85, 2))
plt.grid(axis='y', linestyle=':', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()
# %%
#Perform two-sample t-test
t_stat, p_value = stats.ttest_ind(method_A, method_B)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")