<div align="center">

# 💼 Employee Salary Analyzer

### Intermediate Python Project

A Python-based employee salary analysis system that processes employee salary records, calculates insights, and generates a detailed salary report.

</div>

---

## 📌 Project Overview

The **Employee Salary Analyzer** is a Python project designed to analyze employee salary data and generate meaningful business insights.

The program processes employee records, calculates total earnings, identifies the highest-paid employee, analyzes department-wise salary expenses, evaluates employee performance, and generates a complete salary report.

This project focuses on improving Python problem-solving skills using real-world business scenarios.

---

## 🎯 Objectives

The program performs the following tasks:

* Calculate total earnings of each employee.
* Identify the highest earning employee.
* Calculate total salary expenditure by department.
* Calculate average earnings per employee.
* Assign performance levels based on average earnings.
* Generate a complete employee salary report.

---

## 📂 Dataset Structure

Each employee record contains:

```python
(employee_name, department, salary)
```

Example:

```python
employees = [
    ("Rahul", "IT", 50000),
    ("Anu", "HR", 45000),
    ("Kiran", "IT", 60000),
    ("Priya", "Finance", 55000),
    ("Rahul", "IT", 10000),
    ("Anu", "HR", 5000),
    ("Kiran", "IT", 15000),
    ("Priya", "Finance", 8000)
]
```

---

# 🛠 Project Workflow

## Step 1: Data Preparation

Extract employee information into separate lists:

* Employee Name
* Department
* Salary

Purpose:

* Simplify data processing
* Practice list manipulation
* Prepare data for analysis

---

## Step 2: Calculate Total Earnings

Calculate the total amount earned by each employee, including bonuses.

Example:

```text
Rahul -> 60000
Anu -> 50000
Kiran -> 75000
Priya -> 63000
```

Concepts Used:

* Dictionary Aggregation
* Loops
* Conditional Statements

---

## Step 3: Find Highest Earning Employee

Identify the employee with the highest total earnings.

Example:

```text
Highest Earner:
Kiran -> 75000
```

Concepts Used:

* Maximum Value Search
* Dictionary Traversal

---

## Step 4: Department Salary Analysis

Calculate the total salary expenditure for each department.

Example:

```text
IT -> 135000
HR -> 50000
Finance -> 63000
```

Concepts Used:

* Grouping Data
* Aggregation Logic

---

## Step 5: Calculate Average Earnings

Calculate the average earning per employee.

Formula:

```text
Average Earning = Total Earnings / Number of Salary Entries
```

Example:

```text
Rahul -> 30000
Anu -> 25000
Kiran -> 37500
Priya -> 31500
```

Concepts Used:

* Counting Logic
* Dictionary Operations

---

## Step 6: Performance Evaluation

Assign performance levels using average earnings.

Rules:

| Average Earnings | Performance Level |
| ---------------- | ----------------- |
| ≥ 35000          | Excellent         |
| ≥ 30000          | Good              |
| ≥ 25000          | Average           |
| < 25000          | Needs Improvement |

Example:

```text
Rahul -> Good
Anu -> Average
Kiran -> Excellent
Priya -> Good
```

---

## Step 7: Generate Final Report

The system generates a complete employee report containing:

* Employee Name
* Department
* Total Earnings
* Average Earnings
* Performance Level

Additional Summary:

* Highest Earner
* Department Salary Summary

---

## 🧠 Python Concepts Practiced

This project helped practice:

* Lists
* Tuples
* Dictionaries
* Loops
* Conditional Statements
* Aggregation Logic
* Counting Techniques
* Maximum Value Identification
* Report Generation
* Problem Solving

---

## 📁 Project Structure

```text
employee_salary_analyzer/
│
├── employee_salary_analyzer.py
└── README.md
```

---

## 🚀 Learning Outcomes

Through this project, I learned how to:

* Process structured data efficiently.
* Aggregate information using dictionaries.
* Build multi-step analytical programs.
* Generate professional reports from raw data.
* Solve intermediate-level Python logic problems.

---

## 📈 Skill Level

Project Category:

```text
Intermediate Python Questions
```

Difficulty:

```text
★★★★☆ (4/5)
```

Focus Areas:

* Logical Thinking
* Data Analysis
* Python Problem Solving
* Report Generation

---

## 👨‍💻 Author

**Janardhan M**

Aspiring Data Scientist | Python Learner | AI & Data Science Enthusiast

---

⭐ This project is part of my Python Problem Solving and Data Science preparation journey.

