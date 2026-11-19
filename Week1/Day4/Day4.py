import pandas as pd
# #print(pd.__version__)
# data = {
#   "Name" : ["John", "Navya", "Alex"],
#   "Age" : [33,28,31],
#   "City" : ["Hyderabad", "Dallas", "Seattle"]
# }
# df = pd.DataFrame(data)
#print(df)
# print(df.head())
# print(df.info())
# print(df.describe())

# print(df[df["Age"]>30])
# print(df[df["City"]=="Seattle"])
# print(df[df["Age"]<32])

# df["Experience"] = [8,5,6]
# highest_experience = df[df["Experience"]== df["Experience"].max()]
# print(highest_experience)

# print(df["Experience"].mean)

employee_data = {
    "Name":["Navya","John","Alex","Sarah","Mike"],
    "Salary":[6500,5000,6000,7000,5500],
    "Department":["IT","HR","IT","Finance","IT"]
}
df_employee = pd.DataFrame(employee_data)
#print(df_employee)
print("Total Employees:", df_employee.shape[0])
print("Average Salary:", df_employee["Salary"].mean())
print("Highest Salary:", df_employee["Salary"].max())
print("Lowest Salary:", df_employee["Salary"].min())

print("IT Department Employees:", df_employee["Name"][df_employee["Department"] ==  'IT'])
print("Employees earning more than 6000: ", df_employee["Name"][df_employee["Salary"]> 6000])

print("Highest Salary: ", df_employee["Salary"].max())
largest_department = df_employee["Department"].value_counts().idxmax()
#print(largest_department)
print(f"{largest_department} department has the largest number of employees.")
print("Average Salary: ", df_employee["Salary"].mean())
