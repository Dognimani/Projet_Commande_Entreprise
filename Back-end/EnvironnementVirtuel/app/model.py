from sqlalchemy import column, Integer, String,Float,ForeignKey
from config import Base
from sqlalchemy.orm import relationship
# la table molecule

class Molecule(Base):
    __tablename__ = 'molecule'
    CAS_Number=column(String,primary_key=True)
    Name=column(String)
    Canonical_Formula=column(String)
    Molecular_Weight=column(Float)
    XLogP3=column(Float)
    HydrogenBondDonorCount=column(Float)
    HydrogenBondAcceptorCount=column(Float)
    Rotatable_Bond_Count=column(Float)
    ExactMass=column(Float)
    MonoisotopicMass=column(Float)
    TopologicalPolarSurfaceArea=column(Float)
    Heavy_Atom_Count=column(Float)
    Formal_Charge=column(Float)
    Complexity=column(Float)
    Isotope_Atom_Count=column(Float)
    Undefined_Atom_Stereocenter_Count=column(Float)
    Defined_Bond_Stereocenter_Count=column(Float)
    Undefined_Bond_Stereocenter_Count=column(Float)
    Covalently_Bonded_Unit_Count=column(Float)
    Compound_Is_Canonicalized=column(Float)
    Results = relationship("result",back_populates="Molecules") # mise en place de la clé étrnagère : result= nom de la table enfant et Molecules = le nom de la clé étrangère dans dans la table result

# la table Result
class Result(Base):
    __tablename__ ='result'
    id=column(Integer,primary_key=True)
    Toxicity_Type=column(String)
    value=column(String) # pas sûr que ce soit string mais plutôt text
    CAS_Number=column(String,ForeignKey("molecule.Numero_CAS")) # à revoir poour la partie clé étrangère
    Molecules = relationship("molecule",back_populates="Results") # mapping de la clé étrangère venant de la table molécule


# table Reference
class Reference(Base):
    __tablename__ ='reference'
    id=column(Integer,primary_key=True)
    number=column(Integer)
    value=column(String) # pas sûr que ce soit string mais plutôt text

# table Référencement
class Referencement(Base):
    __tablename__ ='referencement'
    result_id=column(Integer)
    reference_id=column(Integer)
