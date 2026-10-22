import json

# Save Data To JSON File
def save_emp_data(employees):
    with open("employees.json", "w") as file:
        json.dump(employees, file, indent=4)


# Load Json Data
def load_emp_data():
    try:
        with open("employees.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []