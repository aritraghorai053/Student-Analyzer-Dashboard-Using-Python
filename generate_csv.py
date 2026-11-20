
import pandas as pd

names = [
    "Aarav Sharma", "Aditi Das", "Arjun Roy", "Ananya Ghosh",
    "Rohan Sen", "Priya Patel", "Rahul Verma", "Sneha Singh",
    "Ishaan Mishra", "Diya Banerjee", "Aditya Mukherjee",
    "Kavya Dutta", "Vivaan Chatterjee", "Meera Gupta",
    "Reyansh Nair", "Isha Reddy", "Krishna Jain", "Riya Bose",
    "Siddharth Saha", "Anika Kumar", "Kabir Das", "Tanya Roy",
    "Aryan Ghosh", "Neha Sharma", "Shivam Sen", "Ritika Patel",
    "Manav Verma", "Ira Singh", "Dhruv Mishra", "Simran Das",
    "Varun Banerjee", "Tara Mukherjee", "Abhishek Dutta",
    "Madhuri Roy", "Soham Ghosh", "Payal Sen", "Aniket Bose",
    "Shruti Saha", "Saurav Kumar", "Rashmi Jain", "Pranav Nair",
    "Moumita Das", "Kunal Roy", "Nisha Ghosh", "Dev Sharma",
    "Sanya Patel", "Yash Verma", "Pooja Singh", "Ayaan Mishra",
    "Mira Bose", "Riya Sen", "Sourav Das", "Ishita Roy",
    "Rahul Ghosh", "Sanjana Sharma", "Ritwik Sen", "Sohini Das",
    "Arnav Patel", "Tanisha Roy", "Amit Kumar", "Sakshi Verma",
    "Rajat Singh", "Pallavi Ghosh", "Suman Das", "Tushar Roy",
    "Anushka Sen", "Debjit Bose", "Srija Dutta", "Nikhil Sharma",
    "Pritam Das", "Roshni Roy", "Sayan Ghosh", "Rupam Sen",
    "Ishika Patel", "Sagnik Bose", "Mitali Dutta", "Keshav Jain",
    "Anirban Roy", "Sohini Ghosh", "Tanmay Das", "Rhea Sharma",
    "Rishabh Verma", "Sanjay Kumar", "Ayesha Khan", "Omkar Patil",
    "Harsh Mehta", "Snehal Shah", "Akash Yadav", "Komal Gupta",
    "Ritesh Malhotra", "Nandini Iyer", "Gaurav Sinha", "Piyush Agarwal",
    "Swati Mishra", "Deepak Reddy", "Kritika Nair", "Vikram Joshi",
    "Shreya Kapoor", "Mohit Bansal", "Parth Desai", "Avni Mehta",
    "Rohan Malhotra", "Sumanth Rao", "Trisha Kulkarni", "Karan Khanna",
    "Nupur Saxena", "Aman Tiwari", "Bhavna Arora", "Chirag Goel",
    "Jaya Pillai", "Ravi Prasad", "Mansi Thakur", "Varsha Menon",
    "Abhay Tripathi", "Sonal Choudhary", "Naveen Raju", "Ishwar Naik",
    "Anjali Paul", "Siddhi Deshmukh", "Mayank Arora", "Ritika Soni",
    "Karthik Iyer", "Pooja Nambiar", "Suresh Babu", "Diwakar Mishra",
    "Pratik Shah", "Radhika Rao", "Aakash Kulkarni", "Srishti Jain",
    "Nitin Kapoor", "Aparna Nair", "Sahil Khan", "Monika Yadav",
    "Jayant Gupta", "Niharika Bose", "Ashish Sinha", "Payal Mehta",
    "Tarun Joshi", "Sakshi Agarwal", "Anmol Bansal", "Kavita Pillai",
    "Rohit Tripathi", "Shalini Paul", "Uday Menon", "Suman Roy",
    "Riya Mukherjee", "Debashis Saha", "Aritra Ghosh", "Sayan Dutta"
]

departments = ["CSE", "CSE-AIML", "IT", "ECE", "EE", "ME", "CE"]

students = []

for i, name in enumerate(names):
    students.append({
        "Student_ID": f"STU{i+1:03}",
        "Roll_No": f"HIT2026{i+1:03}",
        "Student_Name": name,
        "Department": departments[i % len(departments)]
    })

df = pd.DataFrame(students)

df.to_csv("student_data.csv", index=False)

print("CSV file created successfully!")
print("Total Students:", len(df))
print(df.head(10))
