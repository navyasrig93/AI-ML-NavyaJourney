import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

employee_data = {
  "Name": ["Navya","John","Sarah","Alex","Mike","John"],
  "Department": ["IT","HR","Finance","IT",np.nan,"HR"],
  "Salary": [6500,5000,np.nan,7000,5500,5000],
  "Experience": [8,4,6,10,3,4]
}

df = pd.DataFrame(employee_data)
#print(df)

# Handling Missing Values
missing_dep = df["Department"].isnull().sum()
print(f"Missing Departments: {missing_dep}")

missing_sal = df["Salary"].isnull().sum()
print(f"Missing Salaries:{missing_sal}")

#Replacing Missing Values
df["Department"] = df["Department"].fillna("Unknown")
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

clean_df = df.drop_duplicates()

#print(clean_df)

# Total Employees
total_employees = clean_df.shape[0]
print(f"Total_employees: {total_employees}")

# Average Salary
avg_salary = clean_df["Salary"].mean()
print(f"Average Salary: {avg_salary}")

# Highest Salary
highest_salary = clean_df["Salary"].max()
print(f"Highest Salary: {highest_salary}")

# Lowest Salary
lowest_salary = clean_df["Salary"].min()
print(f"Lowest Salary: {lowest_salary}")

# Average Experience
avg_experience = clean_df["Experience"].mean()
print(f"Average Experience: {avg_experience}")

#Employees per department
employees_per_department = clean_df["Department"].value_counts()
print(f"Employees per Department: {employees_per_department}")

#Highest Paid Employee
highest_salary = clean_df["Salary"].max()
highest_sal_emp = clean_df["Name"][clean_df["Salary"] == highest_salary]
print(f"Highest Paid Employee is {highest_sal_emp.values[0]} with Salary {highest_salary}")

#Employee Count by Department
# employees_per_department.plot(kind = 'bar')
# plt.xlabel('Department')
# plt.ylabel('Number of Employees')
# plt.title('Employee Count by Department')
# plt.show()

#Employee Salary Distribution

# clean_df["Salary"].plot(kind = 'hist')
# plt.xlabel('Salary')
# plt.ylabel('Frequency')
# plt.title('Employee Salary Distribution')
# plt.show()

#Experience Comparison
# clean_df[["Name","Experience"]].plot(kind = 'bar', x= 'Name', y= 'Experience')
# plt.xlabel('Name')
# plt.ylabel('Experience')
# plt.title('Experience Comparison')
# plt.show()

# 1. IT has the highest number of employees.
print(f"{employees_per_department.idxmax()} has the highest number of employees.")
 
# 2. Average salary is above 5500.
if avg_salary > 5500:
    print("Average salary is above 5500.")
else:
    print("Average salary is not above 5500.")
 
# 3. Alex is the highest-paid employee.
print(f"{highest_sal_emp.values[0]} is highest-paid employee.")
 
# 4. Employee experience ranges from 3 to 10 years.
print(f"Employee experience ranges from {clean_df["Experience"].min()} to {clean_df["Experience"].max()}")

# 5. One missing department value was corrected during cleaning.
print(f"{missing_dep} missing department value was corrected.")
