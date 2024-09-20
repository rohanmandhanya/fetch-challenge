from fastapi import APIRouter
from uuid import uuid4

from core import calculate_points
from models import Receipt

router = APIRouter()


data = {}


@router.post("/process")
def receipts_process(payload: Receipt):

    id = str(uuid4())
    data[id] = calculate_points(payload)

    return id


@router.get("/{id}/points")
def get_points(id):

    return {"points": data[id]}
