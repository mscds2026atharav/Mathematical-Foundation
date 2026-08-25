# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# %%
# Normal Distribution
mu = 50
sigma = 10

distribution = norm(loc=mu, scale=sigma)

print("Mean (μ) =", mu)
print("Standard Deviation (σ) =", sigma)

# %%
# (a) Visualization and Theoretical Properties

# %%
# 1. Plot the Probability Density Function (PDF) and Cumulative Distribution Function
# (CDF) of the distribution.

# Plot PDF
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

pdf = distribution.pdf(x)

plt.figure(figsize=(8, 5))
plt.plot(x, pdf)
plt.title("Probability Density Function (PDF)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid()
plt.show()

# %%
# Plot CDF
cdf = distribution.cdf(x)

plt.figure(figsize=(8, 5))
plt.plot(x, cdf)
plt.title("Cumulative Distribution Function (CDF)")
plt.xlabel("Value")
plt.ylabel("Cumulative Probability")
plt.grid()
plt.show()

# %%
# 2. Identify and print the mean, variance, and standard deviation using theoretical formulas.

mean = mu
variance = sigma ** 2
standard_deviation = sigma

print("Theoretical Properties")
print("----------------------")
print("Mean =", mean)
print("Variance =", variance)
print("Standard Deviation =", standard_deviation)


# %%
# (b) Sampling and Empirical Statistics

# %%
# 1. Generate 1000 random samples from the given distribution.
samples = np.random.normal(mu, sigma, 1000)

print("Number of samples generated:", len(samples))
print("First 10 samples:")
print(samples[:10])

# %%
# 2. Plot a histogram of the samples.
plt.figure(figsize=(8, 5))

plt.hist(samples, bins=30, density=True)

plt.title("Histogram of 1000 Random Samples")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid()

plt.show()


# %%
# (c) Probability Computation

# %%
# 1. Compute the probability that a randomly selected value is between 40 and 60.
prob_40_60 = distribution.cdf(60) - distribution.cdf(40)

print("P(40 <= X <= 60) =", prob_40_60)

# %%
# 2. Compute the probability that a value is greater than 65.
prob_greater_65 = 1 - distribution.cdf(65)

print("P(X > 65) =", prob_greater_65)