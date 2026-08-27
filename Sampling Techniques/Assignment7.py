# %%

import pandas as pd

import numpy as np

df = pd.read_csv("Titanic-Dataset.csv")

print(df.head())

print(df.shape)

print(df.info())


# %%

#PART A: Probability-Based Sampling Techniques 

sample_size = int(0.10 * len(df))

print("Original dataset size:", len(df))

print("Sample size:", sample_size)


# %%

# 1. Implement Simple Random Sampling on a real-world dataset (sample size: 10-20%).

simple_random_sample = df.sample(

    n=sample_size,

    random_state=42

)

print("Simple Random Sample:")

print(simple_random_sample.head(10))

print("Sample size:", len(simple_random_sample))


# %%

# 2. Implement Systematic Sampling and extract a sample of similar size.

k = len(df) // sample_size

print("Sampling interval:", k)

systematic_sample = df.iloc[::k].head(sample_size)

print("Systematic Sample:")

print(systematic_sample.head(10))

print("Sample size:", len(systematic_sample))


# %%

#3. Implement Stratified Sampling based on a categorical column (e.g., gender or class).

stratified_sample = (

    df.groupby("Sex", group_keys=False)

      .apply(

          lambda x: x.sample(

              frac=0.10,

              random_state=42

          )

      )

)

print("Stratified Sample:")

print(stratified_sample.head(10))

print("Sample size:", len(stratified_sample))


# %%

#4. Implement Cluster Sampling by selecting complete groups/clusters.

np.random.seed(42)

clusters = df["Pclass"].unique()

selected_cluster = np.random.choice(clusters)

cluster_sample = df[

    df["Pclass"] == selected_cluster

]

print("Selected Cluster:", selected_cluster)

print("Cluster Sample Size:", len(cluster_sample))

print(cluster_sample.head(10))


# %%

# Part B: Non-Probability-Based Sampling Techniques

# %%


#5. Implement Convenience Sampling using accessible or first few records.

convenience_sample = df.head(sample_size)

print("Convenience Sample:")

print(convenience_sample.head(10))

print("Sample size:", len(convenience_sample))


# %%

#6. Implement Purposive (Judgmental) Sampling based on specific criteria.

purposive_sample = df[df["Age"] > 50]

print("Purposive Sample:")

print(purposive_sample.head(10))

print("Sample size:", len(purposive_sample))


# %%

#7. Simulate Snowball Sampling starting from a small group and expanding using a linking attribute.

initial_sample = df.sample(

    n=5,

    random_state=42

)

print("Initial Sample:")

print(initial_sample)

initial_tickets = initial_sample["Ticket"].unique()

print("Initial Tickets:")

print(initial_tickets)

snowball_sample = df[

    df["Ticket"].isin(initial_tickets)

]

print("Snowball Sample:")

print(snowball_sample)

print("Sample size:", len(snowball_sample))


#%%

#8. Implement Quota Sampling by selecting a fixed number of samples from different categories.

male_quota = df[

    df["Sex"] == "male"

].sample(

    n=40,

    random_state=42

)

female_quota = df[

    df["Sex"] == "female"

].sample(

    n=40,

    random_state=42

)

quota_sample = pd.concat([

    male_quota,

    female_quota

])

print("Quota Sample:")

print(quota_sample.head(10))

print("Total sample size:", len(quota_sample))


# %%

#Comparison

comparison = pd.DataFrame({

    "Sampling Technique": [

        "Simple Random",

        "Systematic",

        "Stratified",

        "Cluster",

        "Convenience",

        "Purposive",

        "Snowball",

        "Quota"

    ],

    "Sample Size": [

        len(simple_random_sample),

        len(systematic_sample),

        len(stratified_sample),

        len(cluster_sample),

        len(convenience_sample),

        len(purposive_sample),

        len(snowball_sample),

        len(quota_sample)

    ]

})

print(comparison)