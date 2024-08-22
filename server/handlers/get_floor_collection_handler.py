from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class Floor(BaseModel):
    id: str
    name: str
    level: int
    building_id: str


class GetFloorCollectionResponse(BaseModel):
    floors: List[Floor]


@router.get(
    "/buildings/{building_id}/floors",
    response_model=GetFloorCollectionResponse,
    status_code=200,
)
async def get_floor_collection(building_id: str):
    try:
        return GetFloorCollectionResponse(
            floors=[
                Floor(id="1", name="Floor 1", level=1, building_id=building_id),
                Floor(id="2", name="Floor 2", level=2, building_id=building_id),
                Floor(id="3", name="Floor 3", level=3, building_id=building_id),
            ]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
