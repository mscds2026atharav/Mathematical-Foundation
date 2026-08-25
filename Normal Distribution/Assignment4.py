# %%
# 1. Generate 1000 random IQ scores based on the given distribution.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

num_samples = 1000
mean = 100
std_dev = 15

# Generate 1000 random IQ scores
iq_scores = np.random.normal(mean, std_dev, num_samples)

# Display the first 10 IQ scores
print("First 10 IQ Scores:")
print(iq_scores[:10])


# %%
# 2. Plot a histogram of the IQ scores and overlay the Probability Density Function (PDF).

plt.figure(figsize=(8,5))

# Histogram
plt.hist(iq_scores, bins=30, density=True, color='skyblue', edgecolor='black', alpha=0.7)

# PDF
x = np.linspace(40, 160, 1000)
pdf = norm.pdf(x, mean, std_dev)

plt.plot(x, pdf, color='red', linewidth=2, label='Theoretical PDF')

plt.title("Histogram of IQ Scores with PDF")
plt.xlabel("IQ Score")
plt.ylabel("Density")
plt.legend()
plt.grid(True)

plt.show()


# %%
# 3. Calculate and display the mean, median, and standard deviation of the generated data. Compare them with the theoretical values (100, 15).

sample_mean = np.mean(iq_scores)
sample_median = np.median(iq_scores)
sample_std = np.std(iq_scores)

print("\nDescriptive Statistics")
print("----------------------")
print(f"Mean                : {sample_mean:.2f}")
print(f"Median              : {sample_median:.2f}")
print(f"Standard Deviation  : {sample_std:.2f}")

print("\nTheoretical Values")
print("------------------")
print(f"Theoretical Mean               : {mean}")
print(f"Theoretical Standard Deviation : {std_dev}")


# %%
# 4. Using scipy.stats.norm, compute the probability that an employee's IQ is:

# Less than 90
prob_less_90 = norm.cdf(90, mean, std_dev)

# Greater than 110
prob_greater_110 = 1 - norm.cdf(110, mean, std_dev)

# Between 95 and 105
prob_between = norm.cdf(105, mean, std_dev) - norm.cdf(95, mean, std_dev)

print("\nProbability Calculations")
print("------------------------")
print(f"P(IQ < 90)            = {prob_less_90:.4f}")
print(f"P(IQ > 110)           = {prob_greater_110:.4f}")
print(f"P(95 < IQ < 105)      = {prob_between:.4f}")


# %%
# 5. Plot the Cumulative Distribution Function (CDF) for IQ values ranging from 60 to 140.

x = np.linspace(60, 140, 1000)
cdf = norm.cdf(x, mean, std_dev)

plt.figure(figsize=(8,5))

plt.plot(x, cdf, color='green', linewidth=2)

plt.title("Cumulative Distribution Function (CDF)")
plt.xlabel("IQ Score")
plt.ylabel("Cumulative Probability")
plt.grid(True)

plt.show()