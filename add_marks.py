import pandas as pd
import random

# Read existing student file data
df = pd.read_csv("student_data.csv")

# Add random marks
subjects = ["Mathematics", "Python", "DSA", "COA", "DLD"]

for subject in subjects:
    df[subject] = [random.randint(30, 100) for i in range(len(df))]

#  Save upadated CSV
df.to_csv("student_data.csv",index=False)

print("Student marks added successfully")
print(df.head(10))