import pandas as pd 
df = pd.read_csv("Access_to_Tech_Dataset.csv")

print(df.columns)
print(df.head())

# per-URL values 
# combine multiple violcations into one violation_score per url that identifies by web_URL_id. 
# Currently in my dataset, each row is a violation and same webpage appears multiple times
# , so I will summarize it by using the average score per each website url.

# We do not need to filter out any data because everything already is scraped.
# print(df["scrape_status"].value_counts(dropna=False).head(20)) # scraped    3524

# standardizing 
df["domain_category"] = df["domain_category"].replace({
    "Ecommerce": "E-commerce",
    "TechnologyScienceResearch": "Technology Science and Research"
})

# 2 steps of Aggregation: grouping data and calculating summaries
# step 1: I will combine violations into webpage summary 
# risk_score per webpage
per_url_risk = (
    df.groupby(["web_URL_id", "web_URL", "domain_category"], as_index=False)
      .agg(risk_score=("violation_score", "mean")) # risk_score = avg_violation_score 

)

# serious_critical per webpage 
per_url_sc = (
    df.groupby(["web_URL_id"], as_index=False)
      .agg(
          serious_critical=("violation_impact",
                            lambda s: s.str.lower().isin(["serious","critical"]).sum())
      )
)

# unique_rules_per_url 
per_url_unique = (
    df.groupby(["web_URL_id"], as_index=False)
      .agg(
          unique_rules_per_url=("violation_name", "nunique")
      )
)

# Merge per-URL metrics into one webpage summary table
per_url = (
    per_url_risk
      .merge(per_url_sc, on="web_URL_id", how="left")
      .merge(per_url_unique, on="web_URL_id", how="left")
)
# Optional: total violation rows per URL (nice for sanity checking)
per_url_total = (
    df.groupby(["web_URL_id"], as_index=False)
      .agg(total_violations=("violation_name", "size"))
)
per_url = per_url.merge(per_url_total, on="web_URL_id", how="left")

per_url.to_csv("webpage_metrics.csv", index=False)

# step 2: I will combine webpage into category summary
# Take your webpage-level results and calculate overall statistics for each domain category
df_summary = (
    per_url.groupby("domain_category", as_index=False)
           .agg(
               mean_risk=("risk_score", "mean"),
               std_risk=("risk_score", "std"),
               n=("web_URL_id", "nunique")
           )
           .sort_values("mean_risk", ascending=False)
)

df_summary.to_csv("category_accessibility_summary.csv", index=False)

# Which category worst? Why? Who affected? 
# Worst category = highest mean_risk

# Visualization: Bar chart of mean risk score by domain category
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

plt.figure(figsize=(12,9))

df_summary = df_summary.sort_values("mean_risk", ascending=False)

palette = {
    "E-commerce": "#E57373",
    "Educational Platforms": "#C0A000",
    "Government and Public Services": "#5AAE3F",
    "Health and Wellness": "#5EC9A6",
    "News and Media": "#7EA6E0",
    "Streaming Platforms": "#A68CE6",
    "Technology Science and Research": "#D95ACF"
}

bars = sns.barplot(
    data=df_summary,
    x="domain_category",
    y="mean_risk",
    palette=palette
)

# highlight highest bar with black border
ax = plt.gca()
ax.patches[0].set_edgecolor("black")
ax.patches[0].set_linewidth(3)

plt.xticks(rotation=25, ha='right')

df_summary = df_summary.sort_values("mean_risk", ascending=False)

for i, v in enumerate(df_summary["mean_risk"]):
    plt.text(i, v + 0.03, f"{v:.2f}", ha='center', fontsize=11)

plt.ylim(3.35, 3.8)

plt.title("Which Website Categories Are Most Inaccessible?", fontsize=14)
plt.xlabel("Domain Category")
plt.ylabel("Average Risk Score (per webpage)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

