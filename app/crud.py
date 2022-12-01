from sqlalchemy.orm import Session
from model import Molecule,Result,Reference
from schemas import MoleculeSchema,ReferenceSchema,ResultSchema
import datetime

# get 100 first results
def get_result(db:Session,skip:int=0,limit:int=100):
    return db.query(Result).offset(skip).limit(limit).all()

# get a result by its id   
def get_result_by_id(db:Session,result_id:int):
    return db.query(Result).filter(Result.id==result_id).first()

# create a result    
def create_result(db:Session,result:ResultSchema):
    _result=Result(Toxicity_Type=result.Toxicity_Type,value=result.value,CAS_Number=result.CAS_Number,Created_date=result.Created_date)  
    db.add(_result)      
    db.commit
    db.refresh
    return _result

# remove or delete a result    
def remove_result(db:Session,result_id:int):
    _result=get_result_by_id(db=db,result_id=result_id)
    db.delete(_result)
    db.commit

# update a result    
def update_result(db:Session,result_id:int,Toxicity_Type:str,value:str,CAS_Number:str,Created_date:datetime):
    _result=get_result_by_id(db=db,result_id=result_id)
    _result.Toxicity_Type=Toxicity_Type
    _result.value=value
    _result.CAS_Number=CAS_Number
    _result.Created_date=Created_date 
    db.commit()
    db.refresh(_result) 
    return _result      