from typing import List, Optional, Generic, TypeVar
import datetime
from pydantic import BaseModel, Field,EmailStr
from pydantic.generics import GenericModel


T = TypeVar('T')

class MoleculeSchema(BaseModel):
    CAS_Number: str
    Name : str
    Canonical_Formula : str
    Molecular_Weight:float
    XLogP3 : float
    HydrogenBondDonorCount :float
    HydrogenBondAcceptorCount : float
    Rotatable_Bond_Count :float
    ExactMass : float
    MonoisotopicMass : float
    TopologicalPolarSurfaceArea :float
    Heavy_Atom_Count : float
    Formal_Charge :float
    Complexity:float
    Isotope_Atom_Count:float
    Undefined_Atom_Stereocenter_Count:float
    Defined_Bond_Stereocenter_Count:float
    Undefined_Bond_Stereocenter_Count:float
    Covalently_Bonded_Unit_Count:float
    Compound_Is_Canonicalized : bool


class ResultSchema(BaseModel):
    id : int
    Toxicity_Type : str
    value : str 
    CAS_Number : str
    
#class RequestResult():
    #: ResultSchema = Field(...)



class Response(GenericModel,Generic[T]):
    code:str
    status: str
    message: str
    result:Optional[T]

class ReferenceSchema(BaseModel):
    id : int
    number : int
    value : str 


class UserSchema(BaseModel):
    username: str
    email : EmailStr
    password : str