Week 1 - Day 5
AI/ML Engineer Learning Journey
Student
Navya

Topic
Data Cleaning with Pandas

Learning Objectives
Detect Missing Values
Handle Missing Data
Remove Duplicates
Clean Real-World Datasets
Generate Data-Driven Business Insights
Learn Amazon S3 Fundamentals
Topics Covered
Pandas Data Cleaning
isnull()
sum()
fillna()
dropna()
duplicated()
drop_duplicates()
AWS
Amazon S3
Buckets
Objects
S3 Use Cases
S3 for AI/ML
Exercise 1 - Missing Values
Dataset
data = {
    "Name": ["Navya", "John", "Alex", "Sarah"],
    "Salary": [6500, np.nan, 6000, 7000],
    "Department": ["IT", "HR", np.nan, "Finance"]
}
Functions Used
df.isnull()
df.isnull().sum()
Key Learnings
isnull()
Identifies missing values and returns:

True → Missing Value
False → Valid Value
isnull().sum()
Counts the total number of missing values in each column.

Exercise 2 - Fill Missing Values
Functions Used
df["Salary"] = df["Salary"].fillna(0)

df["Department"] = df["Department"].fillna("Unknown")
Why Use fillna()?
Replacing missing data helps preserve valid information that exists in other columns without deleting the entire record.

Example
Instead of deleting an employee record because salary is missing, we can replace the missing salary and retain employee details.

Exercise 3 - Remove Missing Records
Function Used
clean_df = df.dropna()
Difference Between fillna() and dropna()
fillna()
Replaces missing values while preserving records.

dropna()
Removes rows containing missing values.

Key Learning
Use:

fillna() when data can be reasonably recovered.
dropna() when records are unusable.
Exercise 4 - Remove Duplicates
Dataset
data = {
    "Name": ["Navya", "John", "John", "Alex"],
    "Salary": [6500, 5000, 5000, 6000]
}
Functions Used
df.duplicated()

df.drop_duplicates()
Key Learning
Duplicate detection checks complete rows unless a specific subset of columns is provided.

Mini Project
Employee Data Cleaning Project
Dataset
employee_data = {
    "Name":["Navya","John","John","Sarah","Alex"],
    "Salary":[6500,np.nan,5000,7000,np.nan],
    "Department":["IT","HR","HR",np.nan,"IT"]
}
Data Quality Assessment
Missing Values
Missing Salaries: 2
Missing Departments: 1
Duplicate Analysis
Duplicate Rows: 0
Duplicate Names Investigated
Data Cleaning Performed
Salary Cleanup
Missing salaries replaced with average salary:

df["Salary"].fillna(df["Salary"].mean())
Department Cleanup
Missing departments replaced with:

"Unknown"
Duplicate Cleanup
Removed duplicate records using:

drop_duplicates()
Post-Cleaning Analysis
Metrics Calculated
Total Employees
Average Salary
Highest Salary
Lowest Salary
Statistical Analysis
Performed employee and salary analysis after cleaning the dataset.

Business Insights
Insight 1
Missing salary values were successfully replaced using the average salary to avoid losing employee records.

Insight 2
No fully duplicated employee records were found in the original dataset.

Insight 3
IT remained the largest department based on employee count.

Advanced Investigation
While validating the dataset, duplicate employee names were detected but duplicate rows were not found.

A second dataset was created to test the behavior of:

duplicated()
drop_duplicates()
This helped validate how Pandas identifies duplicate records.

Key Learning
Duplicate names are not always duplicate records.
AWS Learning
Amazon S3
What is Amazon S3?
Amazon Simple Storage Service (S3) is a scalable object storage service used to store and retrieve data from anywhere.

Important Concepts
Bucket
A bucket is a top-level storage container in Amazon S3.

Example:

navya-resume-storage
Object
An object is a file stored inside a bucket.

Examples:

resume.pdf
photo.jpg
sales.csv
S3 Benefits
Highly Durable
Scalable
Secure
Cost Effective
S3 Use Cases
Backup and Recovery
Store backups safely in the cloud.

Media Storage
Store images, videos, and application assets.

Analytics and AI
Store large datasets used for machine learning and analytics.

Why S3 is Important for AI/ML
Amazon S3 acts as a scalable data lake for:

Raw Data
Processed Data
Images
Videos
Model Training Data
Log Files
Machine Learning Artifacts
Challenges Faced
Understanding why duplicate records were not being detected.
Distinguishing between duplicate names and duplicate rows.
Verifying business insights using actual calculations.
Testing alternative datasets to validate duplicate detection.
Key Takeaways
Data cleaning is one of the most important phases of a machine learning project.
Missing values can be handled in multiple ways depending on business requirements.
Duplicate names do not necessarily indicate duplicate records.
Business insights should be generated from data rather than hardcoded.
Amazon S3 is a foundational service for cloud-based AI and machine learning solutions.
