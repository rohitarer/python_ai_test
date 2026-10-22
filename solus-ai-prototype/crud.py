import json


class Employee:
    def __init__(self, name, emp_id, hours):
        self.name = name
        self.emp_id = emp_id
        self.hours = hours

    def to_dict(self):
        return {
            "name" : self.name,
            "id" : self.emp_id,
            "hours": self.hours
        }

    def get_status(self):
        if self.hours >= 9:
            return "Full Day"
        elif self.hours >=4.5:
            return "Half Day"
        return "Absent"

    

# storage

def save_data():
    data = [emp.to_dict() for emp in employees]

    with open("employees2.json", 'w') as file:
        json.dump(data, file, indent=4)


def load_data():
    try:
        with open("employees2.json", 'r') as file:
            data = json.load(file)
        
        return [
            Employee(emp['name'], emp['id'], emp['hours'])
            for emp in data        
        ]

    except FileNotFoundError:
        return []

    
employees = load_data()



# employees = [
#     Employee("Rohit", 101, 9),
#     Employee("Alice", 102, 12),
#     Employee("Sam", 103, 8),
# ]

# Create Employee Details
def get_id(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Enter valid id")

def get_hours(message):
    while True:
        try:
            hours = float(input(message))

            if 0<=hours<=24:
                return hours
            print("Enter the hours between 0 to 24")

        except ValueError:
            print("Enter valid hours")

def create():
    emp_name = input("Enter the employee name ")
    emp_id = get_id("Enter the employee id ")
    worked_hrs = get_hours("Enter the employee worked hours ")

    employees.append(Employee(emp_name, emp_id, worked_hrs))
    save_data()


# Search Emp via Id
def search_id(emp_id):
    for emp in employees:
        if emp.emp_id == emp_id:
            return emp
    return None

# Search Emp via Id
def is_emp_exists():
    code = get_id("Enter the emp code ")

    emp_info = search_id(code)

    if emp_info:
        print(f"{emp_info.name} is found")
    else:
        print("Not found")
        return



# Update emp details
def update():
    code = get_id("Enter the emp code ")
    emp_info = search_id(code)

    if not emp_info:
        print("Not valid emp")
        return

    update_name = input("Update the employee name ")
    update_hours = get_hours("Update the employee worked hours")
    emp_info.name = update_name
    emp_info.hours = update_hours
    save_data()

def delete():
    code = get_id("Enter the emp code ")
    emp_info = search_id(code)

    if not emp_info:
        print("Not valid emp")
        return

    employees.remove(emp_info)
    save_data()

def print_data():

    for emp in employees:
        print(emp.name, emp.emp_id, emp.hours, emp.get_status())


def main():
    while True:
        print("1. Add Employee Details")
        print("2. Search Employee Exists?")
        print("3. Update Employee Details")
        print("4. Delete Employee Details")
        print("5. Print Data")
        print("6. Exit")

        try:
            choice = int(input("Enter the choice "))
        except ValueError:
            print("Invalid choice")
            continue

        if choice == 1:
            create()

        elif choice == 2:
            is_emp_exists()

        elif choice == 3:
            update()

        elif choice == 4:
            delete()

        elif choice == 5:
            print_data()

        elif choice == 6:
            break

        else:
            print('Invalid choice')


if __name__ == "__main__":
    main()

