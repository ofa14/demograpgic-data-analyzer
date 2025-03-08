import pandas as pd

def analyze_data():
    columns = [
        "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
        "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
        "hours-per-week", "native-country", "salary"
    ]
    
    df = pd.read_csv("adult.data", names=columns, sep=",", skipinitialspace=True, na_values=['?'], low_memory=False)
    df['salary_high'] = df['salary'] == '>50K'  

    results = {
        "race_count": df['race'].value_counts(),
        "average_age_men": round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1),
        "percentage_bachelors": round((df['education'] == 'Bachelors').mean() * 100, 1),
        "percentage_advanced_high_income": round(df.loc[df['education'].isin(['Bachelors', 'Masters', 'Doctorate']), 'salary_high'].mean() * 100, 1),
        "percentage_non_advanced_high_income": round(df.loc[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate']), 'salary_high'].mean() * 100, 1),
        "min_work_hours": df['hours-per-week'].min(),
        "percentage_min_workers_high_income": round(df.loc[df['hours-per-week'] == df['hours-per-week'].min(), 'salary_high'].mean() * 100, 1),
        "highest_earning_country": (df.groupby('native-country')['salary_high'].mean() * 100).idxmax(),
        "highest_earning_country_percentage": round((df.groupby('native-country')['salary_high'].mean() * 100).max(), 1),
        "top_occupation_india": df.loc[(df['native-country'] == 'India') & (df['salary_high']), 'occupation'].mode()[0] if not df.loc[(df['native-country'] == 'India') & (df['salary_high'])].empty else "No data"
    }

    return results

if __name__ == "__main__":
    results = analyze_data()
    for key, value in results.items():
        print(f"{key}: {value}")
