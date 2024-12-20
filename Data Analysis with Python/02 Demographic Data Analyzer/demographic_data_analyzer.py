import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # print(df.head())

    # From this point forward, all decimal values will be rounded to 1 decimal space, or 0.1 precision so the ouput mathces the tests.

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df["sex"]=="Male"]["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df.loc[df["education"]=="Bachelors"]) / len(df)) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[(df["education"]=="Bachelors") | (df["education"]=="Masters") | (df["education"]=="Doctorate")]
    lower_education = df.loc[(df["education"]!="Bachelors") & (df["education"]!="Masters") & (df["education"]!="Doctorate")]

    # percentage with salary >50K
    higher_education_rich = round(len(higher_education.loc[higher_education["salary"] == ">50K"]) / len(higher_education) * 100, 1)
    lower_education_rich = round(len(lower_education.loc[lower_education["salary"] == ">50K"]) / len(lower_education) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df["hours-per-week"])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers =len(df.loc[(df["hours-per-week"]==1)&(df["salary"]==">50K")])

    rich_percentage = round(num_min_workers / len(df.loc[df["hours-per-week"]==1]) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    country_group = df.groupby("native-country")
    rich_country_percentage = (country_group["salary"].apply(lambda x: (x == ">50K").sum()) / country_group["salary"].count()) * 100

    highest_earning_country = rich_country_percentage.idxmax()
    highest_earning_country_percentage = round(rich_country_percentage.max(), 1)
    # highest_earning_country = df["salary"].value_counts()["native-country"]
    # highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    rich_india = df.loc[(df["native-country"]=="India")&(df["salary"]==">50K")]
    top_IN_occupation = rich_india["occupation"].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
