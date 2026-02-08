library(dplyr)
library(stringr)
library(tidyr)
library(ggplot2)

# road data and check column
original_df <- read.csv("/Users/parkminji/Access_to_Tech_Dataset.csv")


original_df <- original_df |>
  mutate(
    domain_category = recode(
      domain_category,
      "Ecommerce" = "E-commerce",
      "TechnologyScienceResearch" = "Technology Science and Research"
    )
  )


original_df |> count(domain_category)


# find mean by each category
government_mean <- original_df |>
  filter(domain_category == "Government and Public Services") |>
  summarise(mean_violation = mean(violation_score, na.rm = TRUE)) |>
  pull(mean_violation) |>
  round(2)

news_mean <- original_df |>
  filter(domain_category == "News and Media") |>
  summarise(mean_violation = mean(violation_score, na.rm = TRUE)) |>
  pull(mean_violation) |>
  round(2)

tech_mean <- original_df |>
  filter(domain_category == "Technology Science and Research") |>
  summarise(mean_violation = mean(violation_score, na.rm = TRUE)) |>
  pull(mean_violation) |>
  round(2)

commence_mean <- original_df |>
  filter(domain_category == "E-commerce") |>
  summarise(mean_violation = mean(violation_score, na.rm = TRUE)) |>
  pull(mean_violation) |>
  round(2)

education_mean <- original_df |>
  filter(domain_category == "Educational Platforms") |>
  summarise(mean_violation = mean(violation_score, na.rm = TRUE)) |>
  pull(mean_violation) |>
  round(2)


health_mean <- original_df |>
  filter(domain_category == "Health and Wellness") |>
  summarise(mean_violation = mean(violation_score, na.rm = TRUE)) |>
  pull(mean_violation) |>
  round(2)

stream_mean <- original_df |>
  filter(domain_category == "Streaming Platforms") |>
  summarise(mean_violation = mean(violation_score, na.rm = TRUE)) |>
  pull(mean_violation) |>
  round(2)



# make new df
total_violation_mean_df <- data.frame(
  domain_category = c(
    "Government and Public Services",
    "News and Media",
    "Technology Science and Research",
    "E-commerce",
    "Educational Platforms",
    "Health and Wellness",
    "Streaming Platforms"
  ),
  mean_violation_score = c(
    government_mean,
    news_mean,
    tech_mean,
    commence_mean,
    education_mean,
    health_mean,
    stream_mean
  )
)


# make a bar chart
library("ggplot2")

ggplot(total_violation_mean_df,
       aes(reorder(domain_category, -mean_violation_score), y = mean_violation_score)) +
  geom_bar(stat = "identity") +
  coord_cartesian(ylim = c(3, NA)) +
  labs(
    title = "Total Accessibility Violations by Domain",
    x = "Domain Category",
    y = "Total Violation Score"
  )


