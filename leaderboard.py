import pandas as pd

# Read students data
df = pd.read_csv("student_data.csv")

# Sort students by total marks
top_students = df.sort_values(
    by="Total",
    ascending=False
)

# Display top 10 students
print("\n===== Top 10 Students =====\n")

print(top_students[
    ["Student_ID", "Student_Name", "Department", "Total", "Percentage", "Grade"]].head(10).to_string(index=False)
)

