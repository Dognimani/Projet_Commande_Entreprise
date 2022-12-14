from fastapi import APIRouter,Request,HTTPException,Path,Depends,Form
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import MoleculeSchema,ReferenceSchema,ResultSchema,RequestResult,Response
import crud
from model import Molecule,User, Result
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
    return templates.TemplateResponse("List.html", {"request": request,"molecules":molecules})  



@router.get('/GetMoleculeToUpdate/{CAS_Number}',response_class=HTMLResponse)
async def get_by_id(request:Request,CAS_Number:str,db:Session=Depends(get_db)):
    molecule= db.query(Molecule).filter(Molecule.CAS_Number==CAS_Number).first()
    #_result=crud.get_result_by_id(db,id)    
    return templates.TemplateResponse("MoleculeUpdate.html", {"request": request,"molecule":molecule})  

# update the a specific molecule
@router.post('/MoleculeUpdate/{CAS_Number_param}')
async def update(
    request:Request,
    CAS_Number_param :str,
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
    molecule=db.query(Molecule).filter(Molecule.CAS_Number==CAS_Number_param).first()

    molecule.CAS_Number =CAS_Number,
    molecule.Name = Name    ,
    molecule.Canonical_Formula = Canonical_Formula,
    molecule.Molecular_Weight =Molecular_Weight,           
    molecule.XLogP3 =XLogP3,           
    molecule.HydrogenBondDonorCount =HydrogenBondDonorCount,           
    molecule.HydrogenBondAcceptorCount =HydrogenBondAcceptorCount,           
    molecule.Rotatable_Bond_Count =Rotatable_Bond_Count,           
    molecule.ExactMass = ExactMass,           
    molecule.MonoisotopicMass = MonoisotopicMass,           
    molecule.TopologicalPolarSurfaceArea = TopologicalPolarSurfaceArea,           
    molecule.Heavy_Atom_Count =Heavy_Atom_Count,           
    molecule.Formal_Charge =Formal_Charge,           
    molecule.Complexity =Complexity,           
    molecule.Isotope_Atom_Count =Isotope_Atom_Count,           
    molecule.Undefined_Atom_Stereocenter_Count =Undefined_Atom_Stereocenter_Count,           
    molecule.Defined_Bond_Stereocenter_Count =Defined_Bond_Stereocenter_Count,           
    molecule.Undefined_Bond_Stereocenter_Count =Undefined_Bond_Stereocenter_Count,           
    molecule.Covalently_Bonded_Unit_Count = Covalently_Bonded_Unit_Count,           
    molecule.Compound_Is_Canonicalized = Compound_Is_Canonicalized

    db.commit()
    db.refresh(molecule) 
    molecules=db.query(Molecule).offset(0).limit(4).all()
    return templates.TemplateResponse("List.html", {"request": request,"molecules":molecules})  


@router.get('/MoleculeDetails/{CAS_Number}', response_class=HTMLResponse)
async def GetMoleculeDetails(request:Request,CAS_Number:str,db:Session=Depends(get_db)):
    molecule=db.query(Molecule).filter(Molecule.CAS_Number==CAS_Number).first()
    return templates.TemplateResponse("MoleculeDetails.html", {"request": request,"molecule":molecule})  


@router.get('/DeleteMolecule/{CAS_Number}', response_class=HTMLResponse)
async def delete(request:Request,CAS_Number:str,db:Session=Depends(get_db)):
    print(CAS_Number)
    
    db.query(Result).filter(Result.CAS_Number==CAS_Number).delete()
    db.query(Molecule).filter(Molecule.CAS_Number==CAS_Number).delete()
    #print(molecule.CAS_Number)
    #db.delete(molecule)
    db.commit
    molecules=db.query(Molecule).offset(0).limit(4).all()
    return templates.TemplateResponse("List.html", {"request": request,"molecules":molecules})  



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


#result part
#create an user
# insertion of results part
@router.get('/ToxicologicalProfil/',response_class=HTMLResponse)
async def get_ToxicologicalProfil(request:Request,db:Session=Depends(get_db)):
    molecules=db.query(Molecule).all()
    return templates.TemplateResponse("ToxicologicalProfil.html", {"request": request,"molecules":molecules})  

@router.post('/ResultCreate/',response_class=HTMLResponse)
async def ResultCreate(
    request:Request,
    CAS_Number:str=Form(),
    Toxicity_Type:str=Form(),
    value:str=Form(),
    safe_or_not:str=Form(),
    comment:str=Form(),
    db:Session=Depends(get_db)
    ):
    result=Result(
    CAS_Number=CAS_Number,
    Toxicity_Type=Toxicity_Type,
    value=value,
    safe_or_not=safe_or_not,
    comment=comment
    )
    print(safe_or_not)
    db.add(result)
    db.commit()
    db.refresh(result)
    molecules=db.query(Molecule).all()
    return templates.TemplateResponse("ToxicologicalProfil.html", {"request": request,"molecules":molecules})    