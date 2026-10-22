from fastapi import APIRouter, HTTPException
from models.employees import EmployeeCreate
from store import employees, departments


router = APIRouter(
    prefix= '/employees',
    tags= ['Employees']
)


@router.get("")
def get_emp():
    return {
        "message": "success",
        "data": employees
    }

@router.post("", status_code=201)
def post_emp(employee: EmployeeCreate):
    dept_found = False
    for emp in employees:
        if emp['id'] == employee.id:
            raise HTTPException(
                status_code= 409,
                detail= 'Employee already exists'
            )
    for dept in departments:
        if employee.dept_id == dept['id']:
            dept_found = True
            break

    if not dept_found:
        raise HTTPException(
            status_code= 404,
            detail= 'Department not found'
        )

    employees.append(employee.model_dump())
    return {
        'message': 'success',
        'data': employee
    }