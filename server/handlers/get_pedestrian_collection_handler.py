from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class Pedestrian(BaseModel):
    id: str


class GetPedestrianCollectionResponse(BaseModel):
    pedestrians: List[Pedestrian]


@router.get(
    "/buildings/{building_id}/floors/{floor_id}/pedestrians",
    response_model=GetPedestrianCollectionResponse,
    status_code=200,
)
async def get_pedestrian_collection(building_id: str, floor_id: str):
    try:
        return GetPedestrianCollectionResponse(
            pedestrians=[
                Pedestrian(id="1"),
                Pedestrian(id="2"),
                Pedestrian(id="3"),
            ]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
