import pandas as pd

columns = [
    "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
    "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
    "hours-per-week", "native-country", "salary"
]

df = pd.read_csv("adult.data", names=columns, sep=",", skipinitialspace=True)


df.to_csv("adult.csv", index=False)

print("File successfully converted to CSV!")



# Question 1: How many people of each race are represented in this dataset?
race_count = df['race'].value_counts()

# Question 2: What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean()

# Question 3: What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100

# Question 4: What percentage of people with advanced education make more than 50K?
advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
if advanced_education.shape[0] > 0:
    percentage_advanced_high_income = (advanced_education[advanced_education['salary'] == '>50K'].shape[0] / advanced_education.shape[0]) * 100
else:
    percentage_advanced_high_income = 0  # Handle empty DataFrame

# Question 5: What percentage of people without advanced education make more than 50K?
non_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
if non_advanced_education.shape[0] > 0:
    percentage_non_advanced_high_income = (non_advanced_education[non_advanced_education['salary'] == '>50K'].shape[0] / non_advanced_education.shape[0]) * 100
else:
    percentage_non_advanced_high_income = 0  
# Question 6: What is the minimum number of hours a person works per week?
min_work_hours = df['hours-per-week'].min()

# Question 7: What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_workers = df[df['hours-per-week'] == min_work_hours]
if min_workers.shape[0] > 0:
    percentage_min_workers_high_income = (min_workers[min_workers['salary'] == '>50K'].shape[0] / min_workers.shape[0]) * 100
else:
    percentage_min_workers_high_income = 0  # Handle empty DataFrame

# Question 8: What country has the highest percentage of people that earn >50K, and what is that percentage?
high_income_by_country = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True) * 100
if not high_income_by_country.empty:
    highest_earning_country = high_income_by_country.idxmax()
    highest_earning_country_percentage = high_income_by_country.max()
else:
    highest_earning_country = "No data"
    highest_earning_country_percentage = 0

# Question 9: Identify the most popular occupation for those who earn >50K in India.
high_income_india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
if not high_income_india.empty:
    top_occupation_india = high_income_india['occupation'].value_counts().idxmax()
else:
    top_occupation_india = "No data"

print("1. Race Count:\n", race_count)
print("\n2. Average Age of Men:", round(average_age_men, 1))
print("\n3. Percentage with Bachelors Degree:", round(percentage_bachelors, 1))
print("\n4. Percentage with Advanced Education Earning >50K:", round(percentage_advanced_high_income, 1))
print("\n5. Percentage Without Advanced Education Earning >50K:", round(percentage_non_advanced_high_income, 1))
print("\n6. Minimum Hours Worked Per Week:", min_work_hours)
print("\n7. Percentage of Minimal Workers Earning >50K:", round(percentage_min_workers_high_income, 1))
print("\n8. Country with Highest Percentage Earning >50K:", highest_earning_country, "({}%)".format(round(highest_earning_country_percentage, 1)))
print("\n9. Most Popular Occupation for High Earners in India:", top_occupation_india)                      
