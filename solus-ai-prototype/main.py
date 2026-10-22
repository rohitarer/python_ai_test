from storage import load_emp_data, save_emp_data
from employee import search_id

employees = load_emp_data()

# Add Employee Details
def create_emp():
    emp_name = input("Enter the employee name: ")
    emp_id = int(input("Enter the employee id: "))
    worked_hrs = int(input("Enter the working hours: "))
    
    employees.append({
        "name": emp_name,
        "id": emp_id,
        "hours": worked_hrs
    })
    save_emp_data(employees)

# Check if user exists or not
def is_emp_exists():
    emp_code = int(input("Enter the employee id to check: "))

    if search_id(emp_code, employees):
        print(f"Employee ({emp_code}) exists")
        return True
    else:
        print("Employee data not exists")
        return False

# Update Employee details
def update_details():
    emp_code = int(input("Enter the employee id to update: "))

    emp_info = search_id(emp_code, employees)



    if emp_info:
        update_name = input("Update the name: ")
        update_worked_hrs = int(input("Update the worked hours: "))
        emp_info['name'] = update_name
        emp_info['hours'] = update_worked_hrs
        save_emp_data(employees)
    else:
        print("Employee id invalid")


# Delete Employee
def delete_emp():
    emp_code = int(input("Enter the employee id to delete: "))

    employee = search_id(emp_code, employees)
    if employee:
        employees.remove(employee)
        print(f"Employee {employee['name']} ({employee['id']}) got successfully deleted")
        save_emp_data(employees)
    else:
        print("Employee id invalid")

    
def print_data():
    print(employees)

while True:
    print("1. Add Employee Details")
    print("2. Search Employee Exists?")
    print("3. Update Employee Details")
    print("4. Delete Employee Details")
    print("5. Print Data")
    print("6. Exit")


    try:
        choice = int(input("Enter the choice to continue operation: "))
    except ValueError:
        print("Enter the choices in number")
        continue


    if choice == 1:
        create_emp()

    elif choice == 2:
        is_emp_exists()

    elif choice == 3:
        update_details()

    elif choice == 4:
        delete_emp()

    elif choice == 5:
        print_data()

    elif choice == 6:
        break

    else:
        print('Invalid choice')