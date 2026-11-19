Week 1 - Day 4
AI/ML Engineer Learning Journey
Student
Navya

Topic
Pandas Fundamentals

Learning Objectives
Understand Pandas DataFrames
Explore and Analyze Data
Filter Records
Add and Modify Columns
Generate Business Insights
Learn AWS IAM Fundamentals
Topics Covered
Pandas
DataFrames
Data Exploration
Filtering Data
Adding Columns
Statistical Analysis
Business Insights
AWS
IAM (Identity and Access Management)
IAM Users
IAM Groups
IAM Policies
Root User Best Practices
Exercise 1: DataFrame Basics
Created a DataFrame using a Python dictionary.

Key Learning
A DataFrame is a two-dimensional data structure with rows and columns.

DataFrame vs NumPy Array
DataFrame	NumPy Array
Two-dimensional table structure	Supports multiple dimensions
Can contain different data types	Generally uses a single data type
Includes row and column labels	Uses numeric indexing
Exercise 2: Data Exploration
Used:

df.head()
df.info()
df.describe()
Functions Learned
head()
Displays the first few rows of the dataset.

info()
Shows data types, column information, memory usage, and record counts.

describe()
Provides statistical summaries such as:

Mean
Standard Deviation
Minimum
Maximum
Exercise 3: Filtering Data
Created filters for:

Employees older than 30
Employees living in Seattle
Employees younger than 32
Key Learning
Pandas allows filtering data using conditional expressions.

Example:

df[df["Age"] > 30]
Exercise 4: Adding Columns
Added a new column:

df["Experience"] = [8,5,6]
Calculated
Highest Experience
Average Experience
Key Learning
DataFrames can be modified dynamically by adding new columns.

Mini Project
Employee Data Analyzer
Dataset
{
    "Name":["Navya","John","Alex","Sarah","Mike"],
    "Salary":[6500,5000,6000,7000,5500],
    "Department":["IT","HR","IT","Finance","IT"]
}
Analysis Performed
Salary Metrics
Total Employees
Average Salary
Highest Salary
Lowest Salary
Department Analysis
Employees in IT Department
Employees earning more than 6000
Business Insights
Highest salary in the organization is 7000.
IT department has the largest number of employees.
Average salary is approximately 6000.
AWS IAM Notes
IAM
Identity and Access Management is an AWS service used to securely manage access to AWS resources.

IAM User
Represents an individual user or application that requires AWS access.

IAM Group
A collection of users who share the same permissions.

IAM Policy
A set of permissions that defines what actions are allowed or denied.

Root User
The root account has unrestricted access to all AWS resources and should not be used for daily operations.

Challenges Faced
Understanding DataFrame filtering syntax.
Learning the differences between NumPy arrays and DataFrames.
Interpreting business insights using calculated metrics.
Key Takeaways
Pandas is one of the most important libraries in data analysis and machine learning.
DataFrames are the foundation of real-world data processing.
Business insights should be derived from data rather than hardcoded.
IAM is a critical AWS security service used to manage users and permissions.
Day 4 Review Score
9.4 / 10

Strengths
✅ Strong understanding of DataFrames

✅ Correct use of filtering

✅ Good analytical thinking

✅ Strong AWS IAM concepts

Areas for Improvement
Use .mean() instead of .mean
Continue building dynamic business insights
Keep code clean and well-organized
Progress Tracker
Day 1 - Python Basics
Day 2 - Loops and Functions
Day 3 - NumPy Fundamentals
Day 4 - Pandas Fundamentals
Day 5 - Data Cleaning
Day 6 - Data Visualization
Day 7 - Mini Project
Next Topic
Day 5 - Data Cleaning with Pandas
Topics:

Missing Values
Null Handling
Duplicate Removal
Data Transformations
Real-World Dataset Cleanup
Status: ✅ Day 4 Completed
