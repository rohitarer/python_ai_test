from fastapi import FastAPI, HTTPException
from models import Employee, EmployeeResponse
from routers.employees import router
from store import employees



app = FastAPI()

app.include_router(router)

# @app.get("/")
# def home():
#     return {"message" : "Hello Rohit"}

# @app.get("/about")
# def about():
#     return {"message" : "About - Info"}

# @app.get("/employee/{emp_id}")
# def get_employee(emp_id : int):
#     return {
#         "id" : emp_id,
#         "message" : "Employee Found"
#     }

# @app.get("/employeestime")
# def get_employees(min_hours : float = None):
#     return {
#         "Min Hours" : min_hours
#     }







# @app.post("/employees", status_code = 201)
# def create_employee(employee : Employee):
#     employees.append(employee)
#     return {
#         "message" : "Employee Created",
#         "data" : employee
#     }



# @app.get("/employees/{emp_id}", response_model = EmployeeResponse)
# def get_employee(emp_id : int):
#     for emp in employees:
#         if(emp.id == emp_id):
#             return emp

#     raise HTTPException(
#         status_code= 404,
#         detail = "Employee Not Found"
#     )


# @app.put("/employees/{emp_id}")
# def update_emp(emp_id : int, update_emp : Employee):
#     for emp in employees:
#         if emp.id == emp_id:
#             emp.name = update_emp.name
#             emp.hours = update_emp.hours

#             return {
#                 "message" : "Employee details updated",
#                 "data" : employees
#             }

#     raise HTTPException(
#         status_code= 404,
#         detail= "Employee Not Found"
#     )


# @app.delete("/employees/{emp_id}")
# def delete(emp_id : int):
#     for emp in employees:
#         if emp_id == emp.id:
#             employees.remove(emp)

#             return {
#                 "message" : "Employee remove successfully"
#             }

#     raise HTTPException(
#         status_code= 404,
#         detail= "Employee not found"
#     )