import pandas as pd

# Read student data
df = pd.read_csv("student_data.csv")

# Select subject columns (exclude previously calculated columns)
subjects = [
    col for col in df.select_dtypes(include="number").columns
    if col not in ["Total", "Average", "Percentage"]
]

# Calculate total and average
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

# Calculate percentage
df["Percentage"] = df["Average"]

# Assign grades
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

df["Grade"] = df["Percentage"].apply(calculate_grade)

# Save updated data
df.to_csv("student_data.csv", index=False)

print("Performance analysis completed!")
print(df[["Student_Name", "Total", "Average", "Percentage", "Grade"]].head(10))
