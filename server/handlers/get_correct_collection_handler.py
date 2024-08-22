from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class CorrectPosition(BaseModel):
    id: str
    x: float
    y: float
    direction: float

class GetCorrectPositionCollectionResponse(BaseModel):
    correct_positions: List[CorrectPosition]

@router.get(
    "/buildings/{building_id}/floors/{floor_id}/trajectories/correct-positions",
    response_model=GetCorrectPositionCollectionResponse,
    status_code=200,
)
async def get_correct_position_collection(building_id: str, floor_id: str):
    try:
        return GetCorrectPositionCollectionResponse(
            correct_positions=[
                CorrectPosition(id="1", x=1.0, y=1.0, direction=0.0),
                CorrectPosition(id="2", x=2.0, y=2.0, direction=0.0),
                CorrectPosition(id="3", x=3.0, y=3.0, direction=0.0),
            ]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))