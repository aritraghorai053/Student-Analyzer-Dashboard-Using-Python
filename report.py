import pandas as pd

df = pd.read_csv("student_data.csv")

subjects = [
    col for col in df.select_dtypes(include="number").columns
    if col not in ["Total", "Average", "Percentage"]
]

print("=" * 45)
print("       STUDENT PERFORMANCE REPORT")
print("=" * 45)

print("\nTotal Students:", len(df))
print("Total Departments:", df["Department"].nunique())

print("\nOverall Average:", round(df["Average"].mean(), 2))
print("Highest Marks:", df["Total"].max())
print("Lowest Marks:", df["Total"].min())

print("\nGrade Distribution:")
print(df["Grade"].value_counts().sort_index())

print("\nDepartment Performance:")
print(
    df.groupby("Department")["Average"]
    .mean()
    .round(2)
)

print("\nSubject-wise Average:")
print(df[subjects].mean().round(2))

print("\n" + "=" * 45)
print("          REPORT COMPLETED")
print("=" * 45)