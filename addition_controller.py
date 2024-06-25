from fastapi import APIRouter, HTTPException
from datetime import datetime
from typing import List
from multiprocessing import Pool , cpu_count
from app.models.addition_models import AdditionRequestModel, AdditionResponseModel

router = APIRouter()

@router.post("/addition")

async def perform_addition(request: AdditionRequestModel):
    try:
        payload = request.payload
        batchid = request.batchid
        started_at = datetime.now().isoformat()
        
        with Pool(process = cpu_count()) as pool:
            result = pool.map(sum,payload)
        
        completed_at = datetime.now().isoformat()
        
        response_data = {
            
            "batchid": batchid,
            "ressponse":result,
            "status":"complete",
            "started_at": started_at,
            "completed_at": completed_at
            
        }
        
        return AdditionResponseModel(**response_data)
    
    except Exception as e:
        raise HTTPException(status_code= 500 ,detail=str(e))