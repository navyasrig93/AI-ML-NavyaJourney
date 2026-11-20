import pandas as pd
import numpy as np
# data = {
#   "Name" : ["Navya", "John", "Alex", "Sarah"],
#   "Salary" : [6500, np.nan, 6000, 7000],
#   "Department" : ["IT", "HR", np.nan, "Finance"]
# }
# df = pd.DataFrame(data)
#print(df)
#print(df.isnull())
#print(df.isnull().sum())
# df["Salary"] = df["Salary"].fillna(0)
# df["Department"] = df["Department"].fillna("Unknown")
# print(df)
# clean_df = df.dropna()
# print(clean_df)

# data = {
#   "Name" : ["Navya", "John", "John", "Alex"],
#   "Salary" : [6500, 5000, 5000, 6000]
# }
# df = pd.DataFrame(data)
# #print(df)
# #print(df.duplicated())
# df = df.drop_duplicates()
# print(df)

# employee_data = {
#     "Name":["Navya","John","John","Sarah","Alex"],
#     "Salary":[6500,np.nan,5000,7000,np.nan],
#     "Department":["IT","HR","HR",np.nan,"IT"]
# }

employee_data = {
    "Name":["Navya","John","John","Sarah","Alex","Navya"],
    "Salary":[6500,np.nan,5000.55,7000,np.nan,6500],
    "Department":["IT","HR","HR",np.nan,"IT","IT"]
}

df = pd.DataFrame(employee_data)
print(df)

# print(f"Total Missing Values: {df.isnull().sum()}")

# print(f"Missing Salaries: {df["Salary"].isnull().sum()}")

# print(f"Missing Departments:{df["Department"].isnull().sum()}")

# print(f"Duplicated values: {df.duplicated().sum()}")

#print(f"Duplicated names: {df.duplicated(subset=["Name", "Department"]).sum()}")

average_salary1 = df["Salary"].mean()

#print(average_salary1)

df["Salary"] = df["Salary"].fillna(average_salary1)

Total_num_emp_bef_cleanup = df.shape[0]

print(f"Total number of employees before cleaning: {Total_num_emp_bef_cleanup}")

df["Department"] = df["Department"].fillna("Unknown")

clean_df = df.drop_duplicates()

Total_num_emp_aft_cleanup = clean_df.shape[0]

print(clean_df)

print(f"Total number of employees: {Total_num_emp_aft_cleanup}")

average_salary2 = clean_df["Salary"].mean()
print(f"Average salary : {average_salary2}")

print(f"Highest Salary: {clean_df['Salary'].max()}")

print(f"Lowest Salary: {clean_df['Salary'].min()}")

if average_salary2 > average_salary1:
    print("Average salary increased after cleaning the data.")
else:
    print("Average salary did not increase after cleaning the data.")

if Total_num_emp_bef_cleanup > Total_num_emp_aft_cleanup:
    for i in range(Total_num_emp_bef_cleanup - Total_num_emp_aft_cleanup):
        print(f" {i+1} Employee removed during cleaning.")
    print("Total number of employees decreased after cleaning the data.")
else:
    print("Total number of employees did not decrease after cleaning the data.")

largest_department = clean_df['Department'].value_counts().idxmax()
print(f"{largest_department} remains one of the largest departments.")

    



