from fastapi import APIRouter,Request,HTTPException,Path,Depends,Form
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import MoleculeSchema,ReferenceSchema,ResultSchema,RequestResult,Response
import crud
from model import Resultat,Molecule

#prepa du front
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from pprint import pprint


router = APIRouter()

templates = Jinja2Templates(directory="templates") # specification of the folder of templates (html)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/create1')
async def create(request:RequestResult):
    return {"resquest":request}

@router.post('/create')
async def create(
    Toxicity_Type:str = Form(),
    value:str = Form(),
    CAS_Number:str = Form(),
    db:Session=Depends(get_db)
    ):
    resultat = Resultat(Toxicity_Type = Toxicity_Type, value = value,CAS_Number=CAS_Number)
    db.add(resultat)
    db.commit()
    db.refresh
    #crud.create_result(db,resultat)
    #return templates.TemplateResponse("List.html", {"request": Request})
    return Response(code=200,status="ok",message="result created successfully").dict(exclude_none=True)  
     #return RedirectResponse("http://localhost:8000/")


@router.post('/MoleculeCreate_1/',response_class=HTMLResponse)
async def MoleculeCreate(
    request:Request,
    CAS_Number: str =Form(),
    Name: str =Form(),      
    Canonical_Formula: str =Form(),  
    Molecular_Weight: float =Form(),           
    XLogP3: float =Form(),           
    HydrogenBondDonorCount: float =Form(),           
    HydrogenBondAcceptorCount: float =Form(),           
    Rotatable_Bond_Count: float =Form(),           
    ExactMass: float =Form(),           
    MonoisotopicMass: float =Form(),           
    TopologicalPolarSurfaceArea: float =Form(),           
    Heavy_Atom_Count: float =Form(),           
    Formal_Charge: float =Form(),           
    Complexity: float =Form(),           
    Isotope_Atom_Count: float =Form(),           
    Undefined_Atom_Stereocenter_Count: float =Form(),           
    Defined_Bond_Stereocenter_Count: float =Form(),           
    Undefined_Bond_Stereocenter_Count: float =Form(),           
    Covalently_Bonded_Unit_Count: float =Form(),           
    Compound_Is_Canonicalized: bool =Form(),   
    db:Session=Depends(get_db)
    ):
    molecule = Molecule(
    CAS_Number =CAS_Number,
    Name = Name    ,
    Canonical_Formula = Canonical_Formula,
    Molecular_Weight =Molecular_Weight,           
    XLogP3 =XLogP3,           
    HydrogenBondDonorCount =HydrogenBondDonorCount,           
    HydrogenBondAcceptorCount =HydrogenBondAcceptorCount,           
    Rotatable_Bond_Count =Rotatable_Bond_Count,           
    ExactMass = ExactMass,           
    MonoisotopicMass = MonoisotopicMass,           
    TopologicalPolarSurfaceArea = TopologicalPolarSurfaceArea,           
    Heavy_Atom_Count =Heavy_Atom_Count,           
    Formal_Charge =Formal_Charge,           
    Complexity =Complexity,           
    Isotope_Atom_Count =Isotope_Atom_Count,           
    Undefined_Atom_Stereocenter_Count =Undefined_Atom_Stereocenter_Count,           
    Defined_Bond_Stereocenter_Count =Defined_Bond_Stereocenter_Count,           
    Undefined_Bond_Stereocenter_Count =Undefined_Bond_Stereocenter_Count,           
    Covalently_Bonded_Unit_Count = Covalently_Bonded_Unit_Count,           
    Compound_Is_Canonicalized = Compound_Is_Canonicalized  
    )
    db.add(molecule)
    db.commit()
    db.refresh
    molecules=db.query(Molecule).offset(0).limit(4).all()
    #crud.create_result(db,resultat)
    #return Response(code=200,status="ok",message="result created successfully").dict(exclude_none=True)
    return templates.TemplateResponse("List.html", {"request": request,"molecules":molecules})  
    #return RedirectResponse("http://localhost:8000/")


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
    print("hellllllllllloooooooo")
    _resultat=db.query(Resultat).filter(Resultat.id==id).first()
    print(_resultat.value)
    db.commit
    db.refresh
    #stmt = Resultat.delete().where(Resultat.c.id==24)
    #db.execute(stmt)

   # _result=crud.remove_result(db,result_id=id)
    return Response(code=200,status="ok",message="succes delete data",result=_resultat).dict(exclude_none=True)



# les routes de base en get

# road for the list of molecule
@router.get("/List/", response_class=HTMLResponse)
async def read_molecules(request: Request, db:Session=Depends(get_db)):
    molecules=db.query(Molecule).offset(0).limit(4).all()
    pprint(molecules)
    return templates.TemplateResponse("List.html", {"request": request,"molecules":molecules})  

