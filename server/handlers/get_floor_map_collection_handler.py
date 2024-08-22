from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class FloorMap(BaseModel):
    id: str


class GetFloorMapCollectionResponse(BaseModel):
    floor_maps: List[FloorMap]


@router.get(
    "/buildings/{building_id}/floors/{floor_id}/floor_maps",
    response_model=GetFloorMapCollectionResponse,
    status_code=200,
)
async def get_floor_map_collection(building_id: str, floor_id: str):
    try:
        return GetFloorMapCollectionResponse(
            floor_maps=[
                FloorMap(id="1"),
                FloorMap(id="2"),
                FloorMap(id="3"),
            ]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
