import pandas as pd

# Read student data
df = pd.read_csv("student_data.csv")

# Department-wise analysis
department_status = df.groupby("Department").agg(
    Total_Students=("Student_ID", "count"),
    Average_Marks=("Average", "mean"),
    Highest_Marks=("Average", "max"),
    Lowest_Marks=("Average", "min")
)

# Read decimal values
department_status = department_status.round(2)

print(department_status)

# Highest performing department
best_department = department_status["Average_Marks"].idxmax()

# Lowest performing department
lowest_department = department_status["Average_Marks"].idxmin()

print("\n==== RESULTS =====")
print("Best Department: ", best_department)
print("Lowest Department: ", lowest_department)