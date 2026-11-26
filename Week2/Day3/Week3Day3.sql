select * from emp_data;

create table emp_dept (
	DepartmentID int PRIMARY KEY,
	DepartmentName varchar(50)
)

insert into emp_dept (DepartmentID, DepartmentName)
 values (101, 'IT'),
		(102, 'HR'),
		(103, 'Finance')

Alter table emp_data
add EmpDeptID int;

update a
SET a.EmpDeptID = b.DepartmentID
From emp_data a inner join emp_dept b
on a.EmployeeDept = b.DepartmentName

alter table emp_data
drop column EmployeeDept;

/*Inner Join*/
select a.EmployeeName as Name, b.DepartmentName as Department
from emp_data a inner join emp_dept b
on a.[EmpDeptID] = b.DepartmentID

insert into emp_data([EmployeeID], [EmployeeName], [EmployeeSalary], [EmpDeptID])
values (6, 'Kathy', '6000', NULL )

/*Left Join*/
select a.EmployeeName as Name, b.DepartmentName as Department
from emp_data a left join emp_dept b
on a.[EmpDeptID] = b.DepartmentID

/*Count Employees per deparment*/
select b.DepartmentName, count(a.EmployeeID)
from emp_data a inner join emp_dept b
on a.EmpDeptID = b.DepartmentID
group by b.DepartmentName

/*Average Salary per deparment*/
select b.DepartmentName, AVG(a.EmployeeSalary)
from emp_data a inner join emp_dept b
on a.EmpDeptID = b.DepartmentID
group by b.DepartmentName

/*MAx Salary per deparment*/
select top 1 b.DepartmentName, MAX(a.EmployeeSalary) c
from emp_data a inner join emp_dept b
on a.EmpDeptID = b.DepartmentID
group by b.DepartmentName
order by c desc

print '1. IT department has the highest number of employees.';
 
print '2. IT also has the highest average salary.';
 
print '3. HR has the lowest employee count.';
 
print '4. Most employees belong to technical departments.';
 
print '5. Department data is successfully connected using DepartmentID. Use actual query results.';
