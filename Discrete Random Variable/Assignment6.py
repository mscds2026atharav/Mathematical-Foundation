# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
# (a) Simulate a Discrete Random Variable

# %%
# 1. Simulate 500 rolls of a fair die using random.randint(1, 6) or numpy.random.randint(1, 7,size=500).
rolls_500 = np.random.randint(1, 7, size=500)

# %%
# 2. Display the first 10 outcomes.
print("First 10 outcomes:")
print(rolls_500[:10])

# %%
# (b) Frequency and Visualization

# %%
# 1. Count how many times each number (1 to 6) appears.
numbers = np.arange(1, 7)

frequencies_500 = []

for number in numbers:
    count = np.sum(rolls_500 == number)
    frequencies_500.append(count)

print("Frequency of each number:")
for number, frequency in zip(numbers, frequencies_500):
    print(number, ":", frequency)

# %%
# 2. Plot a bar chart showing the frequency of each outcome.
plt.figure(figsize=(8, 5))

plt.bar(numbers, frequencies_500)

plt.title("Frequency of Die Rolls (500 Rolls)")
plt.xlabel("Die Outcome")
plt.ylabel("Frequency")
plt.xticks(numbers)
plt.grid(axis="y")

plt.show()

# %%
# 3. Which number appeared the most? The least?
most_frequent_number = numbers[np.argmax(frequencies_500)]
least_frequent_number = numbers[np.argmin(frequencies_500)]

most_frequency = max(frequencies_500)
least_frequency = min(frequencies_500)

print("Most frequent number:", most_frequent_number)
print("Frequency:", most_frequency)

print()

print("Least frequent number:", least_frequent_number)
print("Frequency:", least_frequency)

# %%
# (c) Estimating Probabilities

# %%
# 1. Compute the relative frequency (frequency/total) for each outcome.
relative_frequencies_500 = np.array(frequencies_500) / 500

print("Relative frequencies for 500 rolls:")
for number, relative_frequency in zip(numbers, relative_frequencies_500):
    print(number, ":", relative_frequency)

# %%
# 2. Are these probabilities close to the expected value of 1/6?
expected_probability = 1 / 6

print("Expected probability for each number =", expected_probability)
print()

for number, relative_frequency in zip(numbers, relative_frequencies_500):
    difference = abs(relative_frequency - expected_probability)

    print(
        "Number:", number,
        "| Estimated:", round(relative_frequency, 4),
        "| Expected:", round(expected_probability, 4),
        "| Difference:", round(difference, 4)
    )

# %%
# 3. Repeat the experiment with 5000 rolls. Are the estimated probabilities now closer to 1/6?

rolls_5000 = np.random.randint(1, 7, size=5000)

frequencies_5000 = []

for number in numbers:
    count = np.sum(rolls_5000 == number)
    frequencies_5000.append(count)

relative_frequencies_5000 = np.array(frequencies_5000) / 5000

# Display results
print("===== 5000 ROLLS =====")
print("Number   Frequency   Probability")
print("---------------------------------")

for number, frequency, probability in zip(
    numbers, frequencies_5000, relative_frequencies_5000
):
    print(f"{number:<9}{frequency:<12}{probability:.4f}")

print()
print("===== COMPARISON WITH 1/6 =====")
print("Theoretical Probability =", round(expected_probability, 4))
print()

print("Number   500 Rolls   5000 Rolls")
print("--------------------------------")

for i, number in enumerate(numbers):
    print(
        f"{number:<9}"
        f"{relative_frequencies_500[i]:<12.4f}"
        f"{relative_frequencies_5000[i]:.4f}"
    )

print()
print("===== CONCLUSION =====")
print("The estimated probabilities for 5000 rolls")
print("are generally closer to 1/6 than those for 500 rolls.")