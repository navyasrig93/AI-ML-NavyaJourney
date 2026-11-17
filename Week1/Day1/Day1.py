#name = input("Enter the name: ")
#salary = input("Enter the Salary: ")
#annual_salary = int(salary) * 12Navya
#print(f"Annual salary of {name} is {annual_salary}")

#name = input("Enter the name: ")
#age = input("Enter the age:")
#city = input("Enter the city:")
#print(f"Name: {name}, Age: {age}, City: {city}")

# Convert string "100" into integer
# Add 50
# Print result

#number = int("100")
#number = number + 50
#print (number)

Employee_name = input("Enter the employee name: ")
Employee_salary = input ("Enter the employee salary: ")
Annual_salary = int(Employee_salary) * 12
Tax_estimate = int(Annual_salary * 0.1)
Net_salary = int(Annual_salary - Tax_estimate)
print(f"Employee: {Employee_name}, Annual salary: {Annual_salary}, Tax_estimate: {Tax_estimate}, Net_salary: {Net_salary}")
