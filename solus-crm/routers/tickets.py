from fastapi import APIRouter, HTTPException
from models.tickets import TicketCreate, TicketAssign
from store import tickets, departments, employees



router = APIRouter(
    prefix= '/tickets',
    tags= ['Tickets']
)



@router.get("")
def get_tickets():
    return {
        'message': 'success',
        'data': tickets
    }


@router.get("/{tkt_id}")
def get_ticket(tkt_id: int):
    for tkt in tickets:
        if tkt['id'] == tkt_id:
            return tkt
    raise HTTPException(
        status_code= 404,
        detail= "Ticket not found"
    )


@router.post("", status_code=201)
def post_ticket(ticket: TicketCreate):
    dept_found = False

    for tkt in tickets:
        if tkt['id'] == ticket.id:
            raise HTTPException(
                status_code= 409,
                detail= 'Duplicate ticket id found'
            )


    for dpt in departments:
        if dpt['id'] == ticket.dept_id:
            dept_found = True
            break

    if not dept_found:
        raise HTTPException(
            status_code= 404,
            detail= "Invalid department id"
        )
    
    tickets.append(ticket.model_dump())

    return {
        'message': 'success',
        'data': ticket
    }



@router.patch("/{tkt_id}/assign")
def assign_ticket(tkt_id: int, emp_id: TicketAssign):
    selected_ticket= None
    selected_employee = None

    for tkt in tickets:
        if tkt['id'] == tkt_id:
            selected_ticket = tkt
            break
    if not selected_ticket:
        raise HTTPException(
            status_code= 404,
            detail= 'Ticket not found'
        )

    for emp in employees:
        if emp['id'] == emp_id.employee_id:
            selected_employee = emp
            break

    if not selected_employee:
        raise HTTPException(
            status_code= 404,
            detail = 'Employee not found'
        )
    if selected_ticket['dept_id'] == selected_employee['dept_id']:
        selected_ticket['assigned_employee_id'] = selected_employee['id']
        return{
            'data': selected_ticket
        }
    raise HTTPException(
        status_code = 400,
        detail= 'Bad request'
    )