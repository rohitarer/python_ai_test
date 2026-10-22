from models import Ticket, TicketResponse, TicketUpdate
# from store import tickets
from fastapi import APIRouter, HTTPException, Depends
import httpx

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import Base, get_db
from db_models import TicketsDB

router = APIRouter(
    prefix= "/tickets",
    tags= ["Tickets"]
)


@router.post("", status_code= 201)
def create_ticket(ticket: Ticket,
                  db: Session= Depends(get_db)):
    # tickets.append(ticket)
    db_ticket = TicketsDB(
        id = ticket.id,
        title = ticket.title,
        description = ticket.description,
        priority = ticket.priority,
        status = ticket.status,
        assigned_user_id = ticket.assigned_user_id
    )

    db.add(db_ticket)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code = 409,
            detail = "Ticket id already exists"
        )
    db.refresh(db_ticket)
    return {
        "message": "Ticket created successfully",
        "data": db_ticket
    }

def get_tickets_or_404(tkt_id: int,
                       db: Session= Depends(get_db)):
    ticket = db.get(TicketsDB, tkt_id)

    if ticket:
        return ticket

    raise HTTPException(
        status_code = 404,
        detail = "Ticket not found"
    )

@router.get("")
def get_all_tickets(priority: str = None, status: str = None, db: Session= Depends(get_db)):
    results = db.query(TicketsDB)
    if priority:
        results = results.filter(TicketsDB.priority == priority)

    if status:
        results = results.filter(TicketsDB.status == status)

    return results.all()
    # return {
    #     "message": "Tickets List",
    #     "data": tickets
    # }


@router.get("/{tkt_id}", response_model=TicketResponse)
def get_ticket(tkt = Depends(get_tickets_or_404)):
    return tkt


@router.get("/{tkt_id}/assigne")
async def get_user_details(tkt = Depends(get_tickets_or_404)):

    try:
        async with httpx.AsyncClient(timeout = 5.0) as client:
            response = await client.get(
                f"http://127.0.0.1:8002/users/{tkt.assigned_user_id}"
            )

            response.raise_for_status()

            return response.json()
    except httpx.HTTPStatusError as error:
        if error.response.status_code == 404:
            raise HTTPException(
                status_code = 404,
                detail = "User not found"
            )

        raise HTTPException(
            status_code = 502,
            detail = "User API didn't work"
        )
    except httpx.TimeoutException:
        raise HTTPException(
            status_code = 504,
            detail = "API time out"
        )
    except httpx.RequestError:
        raise HTTPException(
            status_code = 503,
            detail = "API request error"
        )
    




# @router.put("/{tkt_id}")
# def update_tkt(update_ticket: TicketUpdate, tkt = Depends(get_tickets_or_404), db: Session=Depends(get_db)):

#     tkt.priority = update_ticket.priority
#     tkt.status = update_ticket.status      

#     db.commit()
#     db.refresh(tkt)

#     return {
#         "message": "Ticket data updated successfully",
#         "data": tkt
#     }

@router.patch("/{tkt_id}")
def update_tkt(update_ticket: TicketUpdate, tkt= Depends(get_tickets_or_404), db: Session= Depends(get_db)):
    updates = update_ticket.model_dump(exclude_unset = True)

    if any(value is None for value in updates.values()):
        raise HTTPException(
            status_code = 422,
            detail = "Field cannot be null"
        )

    for field, value in updates.items():
        setattr(tkt, field, value)

    db.commit()
    db.refresh(tkt)

    return {
        "message": "Ticket field updated successfully.",
        "data": tkt
    }

@router.delete("/{tkt_id}")
def delete(tkt = Depends(get_tickets_or_404), db: Session= Depends(get_db)):

    db.delete(tkt)
    db.commit()

    return {
            "message": "Ticket removed from db succeesfully.",
        }
