from fastapi import APIRouter,HTTPException,Path,Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import MoleculeSchema,ReferenceSchema,ResultSchema,RequestResult,Response
import crud


router = APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/create')
async def create(request:RequestResult,db:Session=Depends(get_db)):
    crud.create_result(db,result=request.parameter)        
    return Response(code=200,status="ok",message="result created successfully").dict(exclude_none=True)  

@router.get('/')
async def get(db:Session=Depends(get_db)):
    _result=crud.get_result(db,0,100)
    return Response(code=200,status="ok",message="succes fetch all data",result=_result).dict(exclude_none=True)

@router.get('/{id}')
async def get_by_id(id:int,db:Session=Depends(get_db)):
    _result=crud.get_result_by_id(db,id)    
    return Response(code=200,status="ok",message="succes get data",result=_result).dict(exclude_none=True)

@router.post('/update/{id}')
async def update(request:RequestResult,db:Session=Depends(get_db)):
    _result=crud.update_result(db,id=request.parameter.id,Toxicity_Type=request.parameter.Toxicity_Type,value=request.parameter.value,CAS_Number=request.parameter.CAS_Number)
    return Response(code=200,status="ok",message="succes update data",result=_result).dict(exclude_none=True)


@router.delete('/delete/{id}')
async def delete(id:int,db:Session=Depends(get_db)):
    _result=crud.remove_result(db,result_id=id)
    return Response(code=200,status="ok",message="succes delete data",result=_result).dict(exclude_none=True)
