from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel




class Building(BaseModel):
    id: str
    name: str
    latitude: float
    longitude: float


class GetBuildingCollectionResponse(BaseModel):
    buildings: List[Building]


router = APIRouter()


@router.get("/buildings", response_model=GetBuildingCollectionResponse, status_code=200)
async def get_building_collection():
    try:
        return GetBuildingCollectionResponse(
            buildings=[
                Building(
                    id="1",
                    name="Building 1",
                    latitude=37.7749,
                    longitude=-122.4194,
                ),
                Building(
                    id="2",
                    name="Building 2",
                    latitude=37.7749,
                    longitude=-122.4194,
                ),
                Building(
                    id="3",
                    name="Building 3",
                    latitude=37.7749,
                    longitude=-122.4194,
                ),
            ]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
