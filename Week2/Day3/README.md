Week 2 - Day 3
SQL Joins & AWS Billing
Student
Navya

Topic
SQL Joins, Table Relationships, and AWS Billing & Pricing

Learning Objectives
Understand Primary Keys
Understand Foreign Keys
Learn INNER JOIN
Learn LEFT JOIN
Connect Multiple Tables
Perform Department Analysis
Learn AWS Billing Concepts
Database Relationships
What is a Primary Key?
A Primary Key uniquely identifies each row in a table.

Examples
EmployeeID
DepartmentID
Rules
Must be unique
Cannot contain duplicate values
Cannot be NULL
What is a Foreign Key?
A Foreign Key creates a relationship between two tables.

Example
DepartmentID
is used to connect:

Employees Table
and

Departments Table
Tables Used
Employees
EmployeeID	Name	DepartmentID
1	Navya	101
2	John	102
3	Alex	101
4	Sarah	103
Departments
DepartmentID	DepartmentName
101	IT
102	HR
103	Finance
Exercise 1 - INNER JOIN
Query
SELECT Employees.Name,
       Departments.DepartmentName
FROM Employees
INNER JOIN Departments
ON Employees.DepartmentID =
   Departments.DepartmentID;
Key Learning
INNER JOIN returns only matching records from both tables.

Result
Navya   IT
John    HR
Alex    IT
Sarah   Finance
Exercise 2 - LEFT JOIN
Query
SELECT Employees.Name,
       Departments.DepartmentName
FROM Employees
LEFT JOIN Departments
ON Employees.DepartmentID =
   Departments.DepartmentID;
Key Learning
LEFT JOIN returns:

All records from the left table
Matching records from the right table
NULL for unmatched records
Example
Mike    NULL
appears because no matching DepartmentID exists.

INNER JOIN vs LEFT JOIN
INNER JOIN	LEFT JOIN
Returns matching records only	Returns all left table records
Excludes unmatched records	Includes unmatched records
Used for clean relationships	Used to preserve missing records
Exercise 3 - Employee Count by Department
Query
SELECT Departments.DepartmentName,
       COUNT(*) AS EmployeeCount
FROM Employees
*NNER JOIN Departments
ON Employees*DepartmentID =
   Departments.Depa*tmentID
GROUP BY Departments.Depar*mentName;
Result
HR        1
Finance   *
Key Learning
JOIN and GOUP BY can be used together to genrate category-level summaries.

--*

Exercise 4 - Average Salary by*Department
Query
SELEC* Departments.DepartmentName,
     * AVG(Employees.Salary)
FROM Employ*es
INNER JOIN Departments
ON Emplo*ees.DepartmentID =
   Departments.*epartmentID
GROUP BY Departments.D*partmentName;
Result
IT        6750
HR        5000
*inance   6000
Key Learnin*
Department-level salary analysishelps compare compensation structues.

Mini Project
Employ*e Department Analysis
Analysis*Performed
Employee & Departme*t Mapping
Connected employee infomation to department names using INER JOIN.

Employee Count by D*partment
IT        2
HR  *     1
Finance   1
Averag* Salary by Department
IT *      6750
HR        5000
Finance * 6000
Highest Paid Depart*ent
IT
Busine*s Insights
Insight 1
IT deparment has the highest number of empoyees with 2 employees.

Insigh* 2
IT department has the highest *verage salary of 6750.

Insight*3
HR department has the lowest av*rage salary of 5000.

Insight 4*
Most employees belong to technica* departments.

Insight 5
Depar*ment information was successfully inked using DepartmentID relationsips.

AWS Learning
AWS B*lling & Pricing
AWS Pricing Mo*el
AWS follows a:

Pay-As*You-Go
pricing model.

Customrs only pay for resources they use

On-Demand Pricing
D*finition
Pay only when resources *re actively used.

Example
``text Use EC2 for 2 hours Pay for 2hours


### Benefits

- No long*term commitment
- Flexible pricing*
---

## Reserved Instances

### D*finition

Commit to AWS resources *or:

```text
1 Year
or
3 Years
```*
### Benefits

- Lower Cost
- Pred*ctable Expenses

---

## AWS Free *ier

AWS provides limited free usa*e for learning purposes.

### Exam*les

- EC2
- S3
- Lambda
- RDS

wi*hin usage limits.

---

# Cost Man*gement Tools

## AWS Billing Dashb*ard

View:

- Current Costs
- Usag* Information
- Service Charges

--*

## AWS Cost Explorer

Analyze sp*nding trends and resource costs.

*--

## AWS Budgets

Create spendin* alerts.

### Example

```text
Ale*t me when monthly cost exceeds $20*
Why Cost Monitoring M*tters
Cost monitoring helps:

P*event unexpected charges
Control*AWS spending
Optimize resource u*age
Improve budget planning
---*

Key Takeaways
✅ Primary Keys u*iquely identify records

✅ Foreign*Keys connect tables

✅ INNER JOIN *eturns matching records

✅ LEFT JO*N preserves unmatched records

✅ JINs enable business and departmentl analysis

✅ AWS uses a Pay-As-Yo*-Go pricing model

✅ Cost monitori*g helps control cloud expenses

--*

Challenges Faced
Understand*ng table relationships.
Differen*iating INNER JOIN and LEFT JOIN. -Interpreting department-level analtics.
Understanding AWS pricing *ptions.
Progress Tracker
*### Week 2

Day 1 - SQL Fund*mentals
Day 2 - SQL Aggregat*ons
Day 3 - SQL Joins
ay 4 - Statistics for Machine Learing
Day 5 - Probability Basi*s
Day 6 - Exploratory Data A*alysis
Day 7 - Portfolio Pro*ect
Technologies Used
S*L
Amazon RDS
Amazon CloudWatch*- AWS Billing Tools
Next T*pic
Day 4 - Statistics for Mac*ine Learning
Topics:

Mean
Me*ian
Mode
Variance
Standard D*viation
Why Statistics Matters i* AI/ML
Created by: Navya* AI/ML Engineer & AWS Learning Jo*rney
