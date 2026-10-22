from models import User
from fastapi import APIRouter, HTTPException
from constants import users_api
import asyncio
import httpx

router = APIRouter(
    prefix = "/users",
    tags = ["Users"]
)

@router.get("")
def get_all_users():
    return{
        "message": "Users List",
    }

@router.get("/{us_id}")
async def get_user(us_id: int):
    try:
        async with httpx.AsyncClient(timeout= 5.0) as client:
            response = await client.get(
                f"{users_api}/{us_id}"
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
            detail = "User Api error"
        )