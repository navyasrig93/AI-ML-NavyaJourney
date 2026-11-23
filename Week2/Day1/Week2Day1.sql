USE LearnWithCopilot
GO
create table emp_data (
EmployeeID int PRIMARY KEY,
EmployeeName varchar(50),
EmployeeDept varchar(10),
EmployeeSalary int
);

insert into emp_data(EmployeeID, EmployeeName, EmployeeDept, EmployeeSalary)
 values 
		--(1, 'Navya', 'IT', 6500),
		--(2, 'John', 'HR', 5000),
		--(3, 'Alex', 'IT', 7000),
		(4, 'Sarah', 'Finance', 6000),
		(5, 'Mike', 'IT', 5500);

select * from emp_data;

select EmployeeName, EmployeeSalary from emp_data;

select * from emp_data where EmployeeDept = 'IT';

select * from emp_data where EmployeeSalary > 5000;

select * from emp_data order by EmployeeSalary asc;

select * from emp_data order by EmployeeSalary desc;

--Show all employees.
select * from emp_data;

--Show only IT employees.
select * from emp_data where EmployeeDept = 'IT';

--Show employees with salary over 6000.
select * from emp_data where EmployeeSalary > 6000;

--Show employees sorted by salary descending.
select * from emp_data order by EmployeeSalary desc;

--Show IT employees earning more than 6000.
select * from emp_data where EmployeeDept = 'IT' and EmployeeSalary > 6000;

PRINT '1. IT department has the highest number of employees.';
PRINT '2. Alex is the highest-paid employee.';
PRINT '3. Multiple employees earn above 6000.';
