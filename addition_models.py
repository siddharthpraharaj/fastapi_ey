from typing import List
from pydantic import BaseModel

class AdditionRequestModel(BaseModel):
    batchid : str
    payload : List[List[int]]
    
class AdditionResponseModel(BaseModel):
    batchid : str
    response : List[int]
    status : str
    started_at : str
    completed_at : str
    
    