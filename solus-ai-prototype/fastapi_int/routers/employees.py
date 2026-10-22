from fastapi import APIRouter, HTTPException, Depends
from models import Employee
from store import employees
import asyncio
import httpx

router = APIRouter(
    prefix = "/employees",
    tags = ['Employees']
)

@router.get("/wait")
async def wait_api():
    await asyncio.sleep(2)

    return {
        "message": "Async usage done"
    }


@router.get("")
def get_all_employees():
    return employees


@router.post("", status_code = 201)
def create_emp(employee: Employee):
    employees.append(employee)
    return {
        "message": "Employee created successfully",
        "data": employee
    }



def get_employee_or_404(emp_id: int):
    for emp in employees:
        if emp_id == emp.id:
            return emp

    raise HTTPException(
        status_code= 404,
        detail = "Employee Not Found"
    )


@router.get("/external-user/{user_id}")
async def get_external_user(user_id : int):

    try:
        async with httpx.AsyncClient(timeout = 5.0) as client:
            response = await client.get(
                f"https://jsonplaceholder.typicode.com/users/{user_id}"
            )

            response.raise_for_status()

            return response.json()
    except httpx.HTTPStatusError as error:
        if error.response.status_code == 404:
            raise HTTPException(
                status_code = 404,
                detail = "Employee not found"
            )

        raise HTTPException(
            status_code = 502,
            detail = "External API response error"
        )
    except httpx.TimeoutException:
        raise HTTPException(
            status_code = 504,
            detail = "External API timeout"
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code = 503,
            detail = "External API exception"
        )

@router.get("/{emp_id}")
def get_employee(emp = Depends(get_employee_or_404)):
    return emp


@router.put("/{emp_id}")
def update_emp(emp_id: int, update_emp: Employee):
    for emp in employees:
        if emp.id == emp_id:
            emp.name= update_emp.name
            emp.hours= update_emp.hours
        
            return {
                "message": "Employee details updated",
                "data": employees
            }

    raise HTTPException(
        status_code=404,
        detail= "Employee Not Found"
    )


@router.delete("/{emp_id}")
def delete(emp_id: int):
    for emp in employees:
        if emp.id == emp_id:
            employees.remove(emp)
            return {
                "message": "Employee deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail= "Employee Not Found"
    )


