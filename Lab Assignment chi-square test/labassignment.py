# %%
#Imports
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns


# %%
# Q1
# Load Titanic dataset
df = sns.load_dataset("titanic")

# Clean 'age' column for accurate sampling
df_age = df.dropna(subset=["age"]).copy()
population_mean_age = df_age["age"].mean()
print(f"True Population Mean Age: {population_mean_age:.2f}\n")


# %%
#1. Implement Simple Random Sampling, Stratified Sampling, and Cluster Sampling on the age column. 


# %%
#Simple Random Sampling (SRS)
srs_sample = df_age["age"].sample(n=100, random_state=42)
srs_mean = srs_sample.mean()
print(f"Simple Random Sample Size: {len(srs_sample)}")
print(f"Simple Random Sample Mean Age: {srs_mean:.2f}")


# %%
# Stratified Sampling (Stratified by 'pclass')
stratified_sample = df_age.groupby("pclass", group_keys=False)["age"].apply(
    lambda x: x.sample(frac=0.2, random_state=42)
)
stratified_mean = stratified_sample.mean()
print(f"Stratified Sample Size: {len(stratified_sample)}")
print(f"Stratified Sample Mean Age: {stratified_mean:.2f}")


# %%
# Cluster Sampling (Clustering by 'pclass')
np.random.seed(42)
all_clusters = df_age["pclass"].unique()
chosen_clusters = np.random.choice(all_clusters, size=2, replace=False)  # Select 2 out of 3 clusters
cluster_sample = df_age[df_age["pclass"].isin(chosen_clusters)]["age"]
cluster_mean = cluster_sample.mean()
chosen_clusters_clean = [int(c) for c in chosen_clusters]

print(f"Selected Clusters (Classes): {chosen_clusters_clean}")
print(f"Cluster Sample Size: {len(cluster_sample)}")
print(f"Cluster Sample Mean Age: {cluster_mean:.2f}")


# %%
#2. Estimate the population mean age using each sampling method. 
# Print Estimated Means
print(f"Simple Random Sample Mean Age: {srs_mean:.2f}")
print(f"Stratified Sample Mean Age:    {stratified_mean:.2f}")
print(f"Cluster Sample Mean Age:       {cluster_mean:.2f}\n")


# %%
#3. Use bootstrapping (resampling with replacement) to estimate the confidence interval for mean age. 
n_iterations = 10000
bootstrap_means = []

for _ in range(n_iterations):
    boot_sample = df_age["age"].sample(frac=1.0, replace=True)
    bootstrap_means.append(boot_sample.mean())

ci_lower = np.percentile(bootstrap_means, 2.5)
ci_upper = np.percentile(bootstrap_means, 97.5)

print(f"95% Confidence Interval for Mean Age: [{ci_lower:.2f}, {ci_upper:.2f}]")


# %%
# Q2

# %%
# 1. Perform a Chi-square test of independence between passenger class (pclass) and survival (survived).
contingency_table = pd.crosstab(df["pclass"], df["survived"])
chi2_stat, p_val_ind, dof, expected = stats.chi2_contingency(contingency_table)

print(f"Contingency Table:\n{contingency_table}\n")
print(f"Chi2 Statistic: {chi2_stat:.4f}")
print(f"p-value:        {p_val_ind:.4e}")
if p_val_ind < 0.05:
    print("Result: Reject H0 — There is a significant association between passenger class and survival.")
else:
    print("Result: Fail to reject H0 — No significant association found.")


# %%
# 2. Perform a Chi-square goodness-of-fit test to check whether the distribution of embarked towns matches expected proportions (e.g., 50% from Southampton, 30% from Cherbourg, 20% from Queenstown).
df_emb = df.dropna(subset=["embarked"])
observed_counts = df_emb["embarked"].value_counts().reindex(["S", "C", "Q"])

total_passengers = observed_counts.sum()
expected_proportions = [0.50, 0.30, 0.20]

# Convert expected counts to clean Python floats rounded to 2 decimal places
expected_counts = [round(float(total_passengers * p), 2) for p in expected_proportions]

chi2_gof, p_val_gof = stats.chisquare(f_obs=observed_counts, f_exp=expected_counts)

print(f"Observed Counts (S, C, Q): {observed_counts.tolist()}")
print(f"Expected Counts (S, C, Q): {expected_counts}")
print(f"Chi2 Statistic:            {chi2_gof:.4f}")
print(f"p-value:                   {p_val_gof}")
if p_val_gof < 0.05:
    print("Result: Reject H0 — Observed embarkation distribution differs significantly from expected proportions.")
else:
    print("Result: Fail to reject H0 — Observed distribution matches expected proportions.")