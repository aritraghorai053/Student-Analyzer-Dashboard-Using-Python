import pandas as pd
import matplotlib.pyplot as plt

# Read student data
df = pd.read_csv("student_data.csv")

# Calculate department-wise average
department_avg = df.groupby("Department")["Average"].mean()

# Create bar chart
plt.figure(figsize=(10,6))

plt.bar(
    department_avg.index,
    department_avg.values
)

# Add labels and title
plt.title("Department-wise Average Performance")
plt.xlabel("Department")
plt.ylabel("Average Marks")

plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Display values above bars
for i, value in enumerate(department_avg.values):
    plt.text(i,value + 1, f"{value:.2f}", ha="center")

plt.tight_layout()
plt.show()


# Top 10 students
top_students = df.sort_values(
    by="Total", ascending=False
).head(10)

plt.figure(figsize=(10, 6))

# Create horizontal bars
plt.barh(
    top_students["Student_Name"],
    top_students["Total"]
)

# Highest marks at the top
plt.gca().invert_yaxis()

# Labels and title
plt.title("Top 10 Students Performance")
plt.xlabel("Total Marks")
plt.ylabel("Student Name")

plt.xlim(0, 500)
plt.grid(axis="x", linestyle="--", alpha=0.5)

# Display marks
for i, value in enumerate(top_students["Total"]):
    plt.text(value + 2, i, str(value), va="center")

plt.tight_layout()
plt.show()


# Grade Distribution Pie Chart

grade_counts = df["Grade"].value_counts().sort_index()

plt.figure(figsize=(8,8))

plt.pie(
    grade_counts.values,
    labels=grade_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Students Grade Distribution")
plt.axis("equal")
plt.show()


# Subject-wise Average Marks

subject_cols = [
    col for col in df.select_dtypes(include="number").columns
    if col not in ["Total", "Average", "Percentage"]
]

subject_avg = df[subject_cols].mean()

plt.figure(figsize=(10, 6))

plt.bar(subject_avg.index, subject_avg.values)

plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.ylim(0, 100)

plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, value in enumerate(subject_avg.values):
    plt.text(i, value + 1, f"{value:.2f}", ha="center")

plt.tight_layout()
plt.show()