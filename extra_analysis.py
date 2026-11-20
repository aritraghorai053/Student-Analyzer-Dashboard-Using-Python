import pandas as pd

df = pd.read_csv("student_data.csv")

topper = df.loc[df["Total"].idxmax()]

print("TOPPER DETAILS")
print("----------------------")
print("Name:", topper["Student_Name"])
print("Department:", topper["Department"])
print("Total Marks:", topper["Total"])
print("Percentage:", topper["Percentage"])
print("Grade:", topper["Grade"])

# Subject with the highest average

subjects = [
    col for col in df.select_dtypes(include="number").columns
    if col not in ["Total", "Average", "Percentage"]
]

subject_avg = df[subjects].mean()

print("\nSUBJECT PERFORMANCE")
print("----------------------")
print(subject_avg)

print("\nBest Subject:", subject_avg.idxmax())
print("Average Marks:", subject_avg.max())

# Students who failed

failed_students = df[df["Grade"] == "F"]

print("\nFAILED STUDENTS")
print("----------------------")

if len(failed_students) == 0:
    print("No students failed!")
else:
    print(failed_students[
        ["Student_ID", "Student_Name", "Department", "Grade"]
    ].to_string(index=False))



# Department topper

department_topper = df.loc[
    df.groupby("Department")["Total"].idxmax()
]

print("\nDEPARTMENT TOPPERS")
print("----------------------")

print(department_topper[
    ["Department", "Student_Name", "Total"]
].to_string(index=False))