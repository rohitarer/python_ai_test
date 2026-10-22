
# Update Employee Details

def search_id(emp_id, employees):
    for emp in employees:
        if emp['id'] == emp_id:
            return emp

    return None