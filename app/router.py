from fastapi import APIRouter,Request,HTTPException,Path,Depends,Form
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import MoleculeSchema,ReferenceSchema,ResultSchema,RequestResult,Response
import crud
from model import Molecule,User #Resultat
#from passlib.hash import sha256_crypt
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

# @router.post('/create')
# async def create(
#     Toxicity_Type:str = Form(),
#     value:str = Form(),
#     CAS_Number:str = Form(),
#     db:Session=Depends(get_db)
#     ):
#     resultat = Resultat(Toxicity_Type = Toxicity_Type, value = value,CAS_Number=CAS_Number)
#     db.add(resultat)
#     db.commit()
# #     db.refresh
#     #crud.create_result(db,resultat)
#     #return templates.TemplateResponse("List.html", {"request": Request})
#     return Response(code=200,status="ok",message="result created successfully").dict(exclude_none=True)  
#     #return RedirectResponse("http://localhost:8000/")

# road for the  molecule registration
@router.get("/MoleculeRegister/", response_class=HTMLResponse)
async def MoleculeRegister(request: Request):
    return templates.TemplateResponse("MoleculeCreate.html", {"request": request})    


#register a molecule
@router.post('/MoleculeCreate/',response_class=HTMLResponse)
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


@router.get('/tttttttttt')
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


@router.get('/delete/{CAS_Number}')
async def delete(request:Request,CAS_Number:str,db:Session=Depends(get_db)):
    print(CAS_Number)
    #_resultat=db.query(Molecule).filter(Molecule.CAS_Number==CAS_Number).first()
    hero = db.get(Molecule,CAS_Number)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    db.delete(hero)
    print(hero.Covalently_Bonded_Unit_Count)
    db.commit
    db.refresh
    molecules=db.query(Molecule).offset(0).limit(4).all()
    return templates.TemplateResponse("List.html", {"request": request,"molecules":molecules})  


# @router.get('/delete_resultat/{id}')
# async def delete(request:Request,id:str,db:Session=Depends(get_db)):
#     print(id)
#     _resultat=db.get(Resultat).filter(Resultat.id==id).first()
#     #hero = db.get(Resultat,id)
#     #if not hero:
#         #raise HTTPException(status_code=404, detail="Hero not found")
#     print(_resultat.value)    
#     db.execute(_resultat)
#     db.commit
#     db.refresh
#     molecules=db.query(Molecule).offset(0).limit(4).all()
#     return templates.TemplateResponse("List.html", {"request": request,"molecules":molecules}) 

# les routes de base en get



# road for the list of molecule
@router.get("/List/", response_class=HTMLResponse)
async def read_molecules(request: Request, db:Session=Depends(get_db)):
    molecules=db.query(Molecule).offset(0).limit(4).all()
    return templates.TemplateResponse("List.html", {"request": request,"molecules":molecules})  

#user part
#create an user
@router.get("/Register/", response_class=HTMLResponse)
async def Register(request: Request):
    return templates.TemplateResponse("Register.html", {"request": request})

#authentication page
@router.get("/", response_class=HTMLResponse)
async def band(request: Request):
    return templates.TemplateResponse("authentication.html", {"request": request}) 

@router.post('/CreateUser',response_class=HTMLResponse)
async def create(
    request:Request,
    Firstname:str = Form(),
    Lastname:str = Form(),
    Email:str = Form(),
    Password:str = Form(),
    db:Session=Depends(get_db)
    ):
    user = User(Firstname = Firstname, Lastname = Lastname,Email=Email, Password=Password)
    db.add(user)
    db.commit()
    db.refresh
    molecules=db.query(Molecule).offset(0).limit(4).all()
    return templates.TemplateResponse("List.html", {"request": request,"molecules":molecules})  

@router.post('/UserAuthentification/',response_class=HTMLResponse)
async def UserAuthentification(
    request:Request,
    Email:str = Form(),
    Password:str = Form(),
    db:Session=Depends(get_db)
    ):
    _user=db.query(User).filter(User.Password==Password).first()
    if _user:
        molecules=db.query(Molecule).offset(0).limit(4).all()
        return templates.TemplateResponse("List.html", {"request": request,"molecules":molecules})
    else:
        return templates.TemplateResponse("authentication.html", {"request": request})  