# 2026 Datathon – Accessibility Risk Analysis
## Project Overview
To answer the question "Which category is worst?" 
This project analyzes web accessibility violations to identify which website
categories present the highest accessibility risk. The analysis aggregates
violation-level data into webpage-level metrics and then into category-level
summaries to compare systemic accessibility challenges.

## Webpage-level Metrics (per_url)
Step 0 — Standardizing categories (data cleaning)
Some categories were written differently but mean the same thing.
Standardizing prevents data from being split into fake categories and makes results accurate.

Step 1 — Violations → Webpage Summary (per URL metrics)
**Metric 1: risk_score (average severity per webpage)
per_url_risk = df.groupby([...]).agg(risk_score=("violation_score","mean"))

risk_score = average violation severity for a webpage
Higher risk_score means the page has more severe accessibility problems overall.

**Metric 2: serious_critical (count of rows where impact is serious or critical)
serious_critical = number of “serious” or “critical” violations on the webpage
This focuses on issues most likely to block disabled users from accessing content.

**Metric 3: unique_rules_per_url (variety of problems)
unique_rules_per_url = number of different accessibility rules broken on a webpage
Higher values mean the page has a wider variety of issues and may be harder to fix.

**Total Violations per page 
total_violations = total number of violation instances on the webpage
Useful for sanity checking and understanding quantity.

Each webpage may contain multiple accessibility violations.  
The table below shows the number of violations detected for selected webpages.

Each row summarizes one webpage (`web_URL_id`) aggregated from multiple accessibility violations.

| web_URL_id | web_URL | domain_category | risk_score | serious_critical | unique_rules_per_url | total_violations |
|---:|---|---|---:|---:|---:|---:|
| 16 | https://www.healthcare.gov | Government and Public Services | 4.00 | 1 | 1 | 1 |
| 17 | https://www.kids.gov | Government and Public Services | 3.25 | 1 | 4 | 4 |
| 20 | https://www.floodsmart.gov | Government and Public Services | 3.00 | 1 | 3 | 3 |
| 21 | https://www.arstechnica.com | News and Media | 3.57 | 4 | 7 | 7 |
| 26 | https://www.popsci.com | News and Media | 4.00 | 5 | 7 | 7 |
| 27 | https://www.discovermagazine.com | News and Media | 3.25 | 1 | 4 | 4 |
| 28 | https://www.newscientist.com | News and Media | 3.00 | 1 | 6 | 6 |
| 30 | https://www.theguardian.com/world | News and Media | 3.29 | 2 | 7 | 7 |
| 33 | https://www.3dcart.com | E-commerce | 4.50 | 4 | 4 | 4 |
| 35 | https://www.weebly.com | E-commerce | 3.50 | 5 | 10 | 10 |

*Full table saved as:* `data/per_url_metrics.csv`

## Category-Level Accessibility Risk Summary
Step 2 — Webpage → Category Summary (per category metrics)
Because to answer “Which category is worst?” you must compare categories, not single pages.
I take the webpage-level table (per_url) and summarize it by category.
mean_risk = average webpage risk in this category
std_risk = how much risk varies across webpages in the category
n = number of webpages analyzed in that category

| domain_category                 | mean_risk | std_risk | n   |
| ------------------------------- | --------- | -------- | --- |
| Educational Platforms           | 3.71      | 0.48     | 114 |
| Technology Science and Research | 3.66      | 0.47     | 121 |
| E-commerce                      | 3.52      | 0.36     | 55  |
| Health and Wellness             | 3.51      | 0.40     | 39  |
| Streaming Platforms             | 3.48      | 0.42     | 76  |
| News and Media                  | 3.45      | 0.23     | 118 |
| Government and Public Services  | 3.42      | 0.34     | 81  |

## Conclusion 
Educational Platforms show the highest average accessibility risk among categories with substantial sample sizes, suggesting systemic accessibility challenges within educational web design that may disproportionately affect users relying on assistive technologies.

