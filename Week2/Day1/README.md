Week 2 - Day 1
SQL Fundamentals for AI/ML Engineers
Student
Navya

Topic
SQL Fundamentals & Amazon RDS

Learning Objectives
Understand Databases
Understand Tables
Learn SQL Queries
Use SELECT Statements
Filter Data using WHERE
Sort Data using ORDER BY
Apply Multiple Conditions
Learn Amazon RDS Fundamentals
Introduction
SQL (Structured Query Language) is used to retrieve, filter, and analyze data stored in databases.

For AI/ML Engineers, SQL is an essential skill because most data used for analytics and machine learning originates from databases.

Typical workflow:

Database
    ↓
SQL
    ↓
Pandas
    ↓
Data Cleaning
    ↓
Machine Learning
Theory
What is a Database?
A database is an organized collection of information that can be stored, managed, and queried efficiently.

Example:

Employee Information
Customer Data
Sales Records
Orders
What is a Table?
A table is a collection of rows and columns used to store related information.

Example
EmployeeID	Name	Department	Salary
1	Navya	IT	6500
2	John	HR	5000
3	Alex	IT	7000
What does SELECT do?
The SELECT statement retrieves data from a table.

Example:

SELECT * FROM Employees;
Meaning of *
The asterisk (*) means:

Return all columns from the table.
Why Select Specific Columns?
Instead of:

SELECT *
FROM Employees;
Use:

SELECT Name, Salary
FROM Employees;
Benefits
Faster execution
Less data transfer
Clearer output
Better performance
What does WHERE do?
The WHERE clause filters rows based on specific conditions.

Example:

SELECT *
FROM Employees
WHERE Department = 'IT';
Why Filtering Matters
Filtering helps businesses focus only on relevant records rather than reviewing entire datasets.

Exercise 1 - SELECT Statements
Retrieve All Employees
SELECT *
FROM Employees;
Purpose
Retrieve all records and columns.

Retrieve Specific Columns
SELECT Name, Salary
FROM Employees;
Purpose
Retrieve only employee names and salaries.

Exercise 2 - WHERE Clause
IT Employees
SELECT *
FROM Employees
WHERE Department = 'IT';
Employees Earning More Than 6000
SELECT *
FROM Employees
WHERE Salary > 6000;
Key Learning
WHERE filters records based on conditions.

Exercise 3 - ORDER BY
Ascending Salary Order
SELECT *
FROM Employees
ORDER BY Salary;
Descending Salary Order
SELECT *
FROM Employees
ORDER BY Salary DESC;
Business Use Cases
Ascending
Identify lower-paid employees.

Descending
Identify highest-paid employees and top performers.

Exercise 4 - Multiple Conditions
SELECT *
FROM Employees
WHERE Department = 'IT'
AND Salary > 6000;
Conditions Applied
Employee must belong to IT Department.
Employee must earn more than 6000.
Mini Project
Employee SQL Analysis
Dataset
EmployeeID	Name	Department	Salary
1	Navya	IT	6500
2	John	HR	5000
3	Alex	IT	7000
4	Sarah	Finance	6000
5	Mike	IT	5500
Query 1
Show All Employees
SELECT *
FROM Employees;
Query 2
Show IT Employees
SELECT *
FROM Employees
WHERE Department = 'IT';
Query 3
Employees Earning More Than 6000
SELECT *
FROM Employees
WHERE Salary > 6000;
Query 4
Sort Employees by Salary
SELECT *
FROM Employees
ORDER BY Salary DESC;
Query 5
IT Employees Earning More Than 6000
SELECT *
FROM Employees
WHERE Department = 'IT'
AND Salary > 6000;
Business Insights
Insight 1
IT is the largest department with 3 employees.

Insight 2
Alex is the highest-paid employee with a salary of 7000.

Insight 3
Two employees earn more than 6000.

Insight 4
IT employees represent 60% of the workforce.

Insight 5
Salary ranges from 5000 to 7000.

AWS Learning
Amazon RDS
What is Amazon RDS?
Amazon Relational Database Service (RDS) is a managed database service that simplifies database administration.

Supported Databases
Amazon RDS supports:

MySQL
PostgreSQL
MariaDB
SQL Server
Oracle
Advantages of Amazon RDS
Automated Backups
AWS automatically manages backups.

Automated Patching
AWS automatically applies updates and patches.

High Availability
Supports failover and database resilience.

Simplified Management
Reduces database administration overhead.

RDS vs EC2 Database
EC2
You manage:

Installation
Backups
Updates
Maintenance
RDS
AWS manages:

Database Setup
Backups
Updates
Infrastructure
Why RDS is Important for AI/ML
RDS stores structured data used for:

Reporting
Analytics
Machine Learning Features
Application Data
It allows AI/ML teams to access reliable and scalable data sources.

Key Takeaways
✅ SQL retrieves data from databases.

✅ SELECT retrieves information.

✅ WHERE filters records.

✅ ORDER BY sorts results.

✅ Multiple conditions can be combined using AND.

✅ Amazon RDS is a managed relational database service.

✅ Databases are a common source of data for AI and Machine Learning projects.

Progress Tracker
Week 2
Day 1 - SQL Fundamentals
Day 2 - SQL Aggregations
Day 3 - SQL Joins
Day 4 - Statistics for Machine Learning
Day 5 - Probability Basics
Day 6 - Exploratory Data Analysis
Day 7 - Week 2 Portfolio Project
Technologies Used
SQL
Amazon RDS
Next Topic
Day 2 - SQL Aggregations
Topics:

COUNT()
SUM()
AVG()
MAX()
MIN()
GROUP BY
Created by: Navya
AI/ML Engineer & AWS Learning Journey
