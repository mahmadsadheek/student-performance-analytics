import pandas as pd
import numpy as np

df = pd.read_csv("students.csv")

subjects = ["Python", "Java", "DBMS", "CN", "OS"]


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_result(average, attendance):
    if average >= 40 and attendance >= 75:
        return "PASS"
    else:
        return "FAIL"


for index, student in df.iterrows():
    marks = np.array([student[subject] for subject in subjects])

    total = np.sum(marks)
    average = np.mean(marks)

    grade = calculate_grade(average)
    result = check_result(average, student["Attendance"])

    print("Student Name:", student["Name"])
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Grade:", grade)
    print("Result:", result)
    print("----------------------------")
print("\n===== PERFORMANCE ANALYSIS =====")

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

top_index = df["Average"].idxmax()
low_index = df["Average"].idxmin()

print("Highest Performer:", df.loc[top_index, "Name"])
print("Highest Average:", round(df.loc[top_index, "Average"], 2))

print("Lowest Performer:", df.loc[low_index, "Name"])
print("Lowest Average:", round(df.loc[low_index, "Average"], 2))

class_average = np.mean(df["Average"])

print("Overall Class Average:", round(class_average, 2))
print("\n===== SUBJECT-WISE ANALYSIS =====")

for subject in subjects:
    average = np.mean(df[subject])
    highest = np.max(df[subject])
    lowest = np.min(df[subject])

    print("\nSubject:", subject)
    print("Average Marks:", round(average, 2))
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)

best_subject = df[subjects].mean().idxmax()
worst_subject = df[subjects].mean().idxmin()

print("\nBest Performing Subject:", best_subject)
print("Lowest Performing Subject:", worst_subject)
print("\n===== PASS AND FAIL STATISTICS =====")

pass_count = 0
fail_count = 0

for index, student in df.iterrows():
    average = student["Average"]
    attendance = student["Attendance"]

    if average >= 40 and attendance >= 75:
        pass_count += 1
    else:
        fail_count += 1

print("Total Students:", len(df))
print("Students Passed:", pass_count)
print("Students Failed:", fail_count)
print("Pass Percentage:", round(pass_count / len(df) * 100, 2), "%")
print("\n========== STUDENT PERFORMANCE REPORT ==========")

df["Grade"] = df["Average"].apply(calculate_grade)
df["Result"] = df.apply(
    lambda student: check_result(
        student["Average"], student["Attendance"]
    ),
    axis=1
)

print(df[[
    "Student_ID",
    "Name",
    "Total",
    "Average",
    "Grade",
    "Attendance",
    "Result"
]].to_string(index=False))

print("\n========== REPORT COMPLETED ==========")