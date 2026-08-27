# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import chisquare
from scipy.stats import chi2_contingency


# %%

# PART A: Chi-Square Goodness of Fit Test

# Observed frequencies of candy colors

colors = ["Red", "Blue", "Green", "Yellow", "Orange"]

observed = np.array([28, 30, 20, 12, 10])

# Company's claimed proportions

claimed_proportions = np.array([0.30, 0.25, 0.20, 0.15, 0.10])

# Total number of candies

total = observed.sum()

# Calculate expected frequencies

expected = total * claimed_proportions

print("Total candies:", total)

print("Observed frequencies:", observed)

print("Expected frequencies:", expected)


# %%

# Create a table

goodness_of_fit_table = pd.DataFrame({

    "Color": colors,

    "Observed": observed,

    "Expected": expected

})

print("Goodness of fit table for colour of candies")
print(goodness_of_fit_table)


# %%

#Null and alternate hypothesis for candies problem
print("Null hypothesis: The observed candy color distribution follows the company's claimed proportions.")
print("Alternate hypothesis: The observed candy color distribution is significantly different from the company's claimed proportions.")


# %%

# Perform Chi-Square Goodness of Fit Test

chi_square_stat, p_value = chisquare(

    f_obs=observed,

    f_exp=expected

)

print("Chi-Square Statistic:", chi_square_stat)

print("P-value:", p_value)


# %%

# Significance level

alpha = 0.05

if p_value < alpha:

    print("Reject the Null Hypothesis.")

    print("The observed color distribution is significantly different from the company's claim.")

else:

    print("Fail to Reject the Null Hypothesis.")

    print("There is not enough evidence to say that the color distribution differs from the company's claim.")


# %%

# Visualization for Goodness of Fit Test

x = np.arange(len(colors))

width = 0.35

plt.figure(figsize=(10, 6))

plt.bar(
    x - width/2,
    observed,
    width,
    label="Observed"
)

plt.bar(
    x + width/2,
    expected,
    width,
    label="Expected"
)

plt.xlabel("Candy Color")

plt.ylabel("Frequency")

plt.title("Observed vs Expected Candy Color Distribution")

plt.xticks(x, colors)

plt.legend()

plt.show()


# %%

# PART B: Chi-Square Test of Independence

# Create contingency table

social_media_data = pd.DataFrame(

    [

        [20, 18, 7],

        [10, 15, 8],

        [5, 8, 9],

        [2, 4, 4]

    ],

    index=[
        "Instagram",
        "Twitter",
        "Facebook",
        "LinkedIn"
    ],

    columns=[
        "15-20",
        "21-25",
        "26-30"
    ]

)

print("Contingency Table:")

print(social_media_data)


# %%

#Null and alternate hypothesis for social media problem

print("Null hypothesis: Age group and preferred social media platform are independent; there is no significant association.")
print("Alternate hypothesis: Age group and preferred social media platform are not independent; there is a significant association.")

# %%

# Perform Chi-Square Test of Independence

chi_square_stat, social_p_value, degrees_of_freedom, expected_frequencies = chi2_contingency(

    social_media_data

)

print("Chi-Square Statistic:", chi_square_stat)

print("P-value:", social_p_value)

print("Degrees of Freedom:", degrees_of_freedom)


# %%

# Display expected frequencies

expected_table = pd.DataFrame(

    expected_frequencies,

    index=social_media_data.index,

    columns=social_media_data.columns

)

print("Expected Frequencies:")

print(expected_table)


# %%

# Hypothesis Testing

alpha = 0.05

if social_p_value < alpha:

    print("Reject the Null Hypothesis.")

    print("There is a significant association between age group and preferred social media platform.")

else:

    print("Fail to Reject the Null Hypothesis.")

    print("There is no significant association between age group and preferred social media platform.")


# %%

# Grouped Bar Chart

social_media_data.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Preferred Social Media Platform by Age Group")

plt.xlabel("Social Media Platform")

plt.ylabel("Number of Students")

plt.xticks(rotation=0)

plt.legend(title="Age Group")

plt.show()
# %%
