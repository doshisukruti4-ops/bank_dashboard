import pandas as pd


df = pd.read_csv("your_file.csv")


# View the first 5 rows
print("--- FIRST 5 ROWS (HEAD) ---")
print(df.head())

# View the last 5 rows
print("\n--- LAST 5 ROWS (TAIL) ---")
print(df.tail())

# List all column names
print("\n--- COLUMN NAMES ---")
print(df.columns)

# Check data types of all columns
print("\n--- DATA TYPE OF ALL COLUMNS ---")
print(df.dtypes)

#filling missing values
df = df.fillna(0)

# Remove duplicate rows
df = df.drop_duplicates()

# Correct format: Remove accidental spaces and fix text columns to UPPERCASE
df["card_type"] = df["card_type"].str.strip().str.upper()
df["geography"] = df["geography"].str.strip().str.upper()
df["gender"] = df["gender"].str.strip().str.upper()

# Calculate the mean (average) of Credit Score
avg_credit = df["creditscore"].mean()
print(f"\nAverage Credit Score: {avg_credit}")

# Calculate the mean (average) of Estimated Salary
avg_salary = df["estimatedsalary"].mean()
print(f"Average Estimated Salary: {avg_salary}")

# Summary of averages for all numeric columns at once
print("\n--- AVERAGE (MEAN) OF ALL NUMERIC COLUMNS ---")
print(df.mean(numeric_only=True))
