Week 2 - Day 2
SQL Aggregations & Data Summaries
Student
Navya

Topic
SQL Aggregation Functions & Amazon CloudWatch

Learning Objectives
Understand SQL Aggregation Functions
Perform Data Summarization
Analyze Business Metrics
Group Data Using GROUP BY
Generate Business Insights
Learn AWS CloudWatch Fundamentals
Introduction
Aggregation functions allow businesses to summarize large datasets into meaningful metrics.

Instead of reviewing thousands of records individually, organizations use aggregation functions to answer questions like:

How many employees are there?
What is the average salary?
What is the highest salary?
How much is the total salary expense?
How many employees belong to each department?
SQL Aggregation Functions
COUNT()
Query
SELECT COUNT(*)
FROM Employees;
Result
*```text 5


### Purpose

Returns the total number of employee records.

### Key Learning

COUNT() is used to count records in a table.

---

## AVG()

### Query

```sql
SELECT AVG(Salary)
FROM Employees;
Result
6000
Purpose
Calculates the average salary across all employees.

Business Value
Average salary helps organizations:

Analyze compensation
Budget effectively
Compare salaries against market standards
MAX()
Query
SELECT MAX(Salary)
FROM Employees;
Result
7000
Purpose
Finds the highest salary in the organization.

MIN()
Query
SELECT MIN(Salary)
FROM Employees;
Result
5000
Purpose
Finds the lowest salary in the organization.

SUM()
Query
SELECT SUM(Salary)
FROM Employees;
Result
30000
Purpose
Calculates the total salary expense.

Business Value
Helps management:

Estimate payroll costs
Plan budgets
Forecast future expenses
GROUP BY Analysis
Employee Count by Department
Query
SELECT Department,
       COUNT(*)
FROM Employees
GROUP BY Department;
Result
IT        3
HR        1
Finance   1
Key Learning
GROUP BY organizes records into categories for analysis.

Average Salary by Department
Query
SELECT Department,
       AVG(Salary)
FROM Employees
GROUP BY Department;
Result
IT        6333
HR        5000
Finance   6000
Key Learning
Department-level analysis helps organizations compare compensation structures.

Mini Project
Employee Salary Analytics
Dataset
EmployeeID	Name	Department	Salary
1	Navya	IT	6500
2	John	HR	5000
3	Alex	IT	7000
4	Sarah	Finance	6000
5	Mike	IT	5500
Metrics Calculated
Total Employees
5
Average Salary
6000
Highest Salary
7000
Lowest Salary
5000
Total Salary Expense
30000
Department Analysis
Employee Count
IT        3
HR        1
Finance   1
Average Salary by Department
IT        6333
HR        5000
Finance   6000
Business Insights
Insight 1
IT department has the highest employee count with 3 employees.

Insight 2
The average employee salary is 6000.

Insight 3
Salary ranges between 5000 and 7000.

Insight 4
The organization spends 30000 on employee salaries.

Insight 5
IT department has the highest average salary among all departments.

AWS Learning
Amazon CloudWatch
What is Amazon CloudWatch?
Amazon CloudWatch is a monitoring and observability service for AWS resources and applications.

What CloudWatch Monitors
EC2
CPU Utilization
Memory Usage
Network Traffic
Lambda
Invocations
Errors
Execution Duration
RDS
Storage Consumption
Database Connections
Performance Metrics
CloudWatch Metrics
Metrics are time-ordered measurements used to monitor resource performance.

Examples:

CPU Utilization
Request Count
Memory Usage
CloudWatch Alarms
Alarms monitor metrics and trigger actions when thresholds are exceeded.

Example:

Send notification when CPU usage exceeds 80%
Why Monitoring Matters
Monitoring helps organizations:

Detect issues early
Improve reliability
Optimize performance
Control costs
Monitor AI/ML workloads
Key Takeaways
✅ COUNT() counts records

✅ AVG() calculates averages

✅ MAX() identifies highest values

✅ MIN() identifies lowest values

✅ SUM() calculates totals

✅ GROUP BY categorizes data

✅ CloudWatch monitors AWS resources

✅ Metrics and alarms improve operational visibility

Challenges Faced
Understanding how aggregation functions summarize data.
Converting metrics into business insights.
Interpreting departmental salary analysis.
Progress Tracker
Week 2
Day 1 - SQL Fundamentals
Day 2 - SQL Aggregations
Day 3 - SQL Joins
Day 4 - Statistics for Machine Learning
Day 5 - Probability Basics
Day 6 - Exploratory Data Analysis
Day 7 - Portfolio Project
Technologies Used
SQL
Amazon RDS
Amazon CloudWatch
Next Topic
Day 3 - SQL Joins
Topics:

INNER JOIN
LEFT JOIN
RIGHT JOIN
Combining Multiple Tables
Real-World Database Relationships
Created by: Navya
AI/ML Engineer & AWS Learning Journey
