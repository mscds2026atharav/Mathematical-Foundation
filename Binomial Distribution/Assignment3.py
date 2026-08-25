# (a) Simulate a Binomial Random Variable
# %%
# 1. Simulate 1000 experiments of flipping a fair coin 10 times.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

num_experiments = 1000
num_flips = 10
p = 0.5

# Simulate 1000 experiments
heads = np.random.binomial(num_flips, p, num_experiments)

# 2. Display the first 10 outcomes (i.e., number of heads per experiment).
print("First 10 outcomes (number of heads in each experiment):")
print(heads[:10])

# %%
# (b) Frequency and Visualization

# Count frequency for the first 100 experiments
frequency_100 = np.bincount(heads[:100], minlength=11)

# Count frequency for all 1000 experiments
frequency = np.bincount(heads, minlength=11)

# 1. Count how many times each value (from 0 to 100) appears.
print("\nFrequency Table (First 100 Experiments)")
print("---------------------------------------")
print("Heads\tNumber of Experiments")

for i in range(11):
    print(f"{i}\t{frequency_100[i]}")

# 2. Count how many times each value (from 0 to 1000) appears.
print("\nFrequency Table (All 1000 Experiments)")
print("--------------------------------------")
print("Heads\tNumber of Experiments")

for i in range(11):
    print(f"{i}\t{frequency[i]}")

# 3. Plot a bar chart of the frequency distribution.
plt.figure(figsize=(8,5))
plt.bar(range(11), frequency, color='skyblue', edgecolor='black')

plt.title("Frequency Distribution of Number of Heads ( 1000 experiments )")
plt.xlabel("Number of Heads")
plt.ylabel("Frequency")
plt.xticks(range(11))
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

# %%
# (c) Estimating Probabilities

# 1. Compute the relative frequency for each value.
relative_frequency = frequency / num_experiments

# 2. Compare these with the theoretical binomial probabilities.
theoretical_probability = binom.pmf(np.arange(11), num_flips, p)

print("\nHeads\tFrequency\tRelative Freq\tTheoretical Prob")
for i in range(11):
    print(f"{i}\t{frequency[i]}\t\t{relative_frequency[i]:.4f}\t\t{theoretical_probability[i]:.4f}")

# 3. Comment on how closely the simulation matches theory.
print("\nConclusion:")

difference = np.abs(relative_frequency - theoretical_probability)

if np.all(difference < 0.03):
    print("The simulated probabilities are very close to the theoretical binomial probabilities.")
    print("Small differences are due to random variation in the simulation.")
else:
    print("There are noticeable differences between the simulated and theoretical probabilities.")
    print("Increasing the number of experiments will make the simulation closer to the theoretical distribution.")
# %%
