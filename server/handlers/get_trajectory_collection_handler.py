from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class Trajectory(BaseModel):
    id: str

class GetTrajectoryCollectionResponse(BaseModel):
    trajectories: List[Trajectory]


@router.get(
    "/buildings/{building_id}/floors/{floor_id}/trajectories",
    response_model=GetTrajectoryCollectionResponse,
    status_code=200,
)
async def get_trajectory_collection(building_id: str, floor_id: str):
    try:
        return GetTrajectoryCollectionResponse(
            trajectories=[
                Trajectory(id="1"),
                Trajectory(id="2"),
                Trajectory(id="3"),
            ]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))