from fastapi import APIRouter, HTTPException
from models.departments import createDepartment
from store import departments

router = APIRouter(
    prefix = '/departments',
    tags = ['Departments']
)


@router.get("")
def get_departments():
    return {
        "departments" : departments
    }

@router.get("/{dept_id}")
def get_dept(dept_id: int):
    for dpt in departments:
        if dpt['id'] == dept_id:
            return dpt
    raise HTTPException(
        status_code= 404,
        detail= 'Department not found'
    )

@router.post("", status_code=201)
def post_dept(department: createDepartment):
    dept_found = False
    for dpt in departments:
        if dpt['id'] == department.id:
            raise HTTPException(
                status_code= 409,
                detail= "Department already exists"
            )
    departments.append(department.model_dump())
    return {
        'message': "success",
        'data': department
    }

