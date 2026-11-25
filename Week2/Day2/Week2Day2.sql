USE LearnWithCopilot
select * from emp_data;

/*Count all employees */
select count(EmployeeID) from emp_data;

/*Find average salary:*/
select avg(EmployeeSalary) from emp_data;

/*Highest Salary*/
select max(EmployeeSalary) from emp_data;

/*Lowest Salary*/
select min(EmployeeSalary) from emp_data;

/*Total Salary*/
select sum(EmployeeSalary) from emp_data;

/*Number of employees in each department*/
select [EmployeeDept], count(*)
from [dbo].[emp_data]
group by [EmployeeDept]

/*Average salary by department*/
select EmployeeDept, AVG(EmployeeSalary)
from emp_data
group by EmployeeDept

/*1. IT department has the highest employee count.

2. IT also has the highest total salary expense.

3. Average salary across the organization is above 6000.

4. Salary ranges from 5000 to 7000.

5. The organization spends 30000 annually on employee salaries.*/

print 'IT department has the highest employee count.';
print 'IT also has the highest total salary expense.';
print 'Salary ranges from 5000 to 7000.';
print 'The organization spends 30000 annually on employee salaries.'
