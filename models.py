from pydantic import BaseModel
from typing import List

# What agent sees
class Observation(BaseModel):
    user_id: int
    history: List[int]  # previously viewed products


# What agent does
class Action(BaseModel):
    recommended_product: int  # product ID


# Reward returned by environment
class Reward(BaseModel):
    score: float  # between -1 and 1