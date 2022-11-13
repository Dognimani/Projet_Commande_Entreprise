from sqlalchemy import Column, Integer, String,Float,ForeignKey,DateTime, Boolean, Table
from config import Base, engine
from sqlalchemy.orm import relationship
import datetime
# la table molecule

class Molecule(Base):
    __tablename__ = 'molecules'
    CAS_Number=Column(String,primary_key=True)
    Name=Column(String)
    Canonical_Formula=Column(String)
    Molecular_Weight=Column(Float)
    XLogP3=Column(Float)
    HydrogenBondDonorCount=Column(Float)
    HydrogenBondAcceptorCount=Column(Float)
    Rotatable_Bond_Count=Column(Float)
    ExactMass=Column(Float)
    MonoisotopicMass=Column(Float)
    TopologicalPolarSurfaceArea=Column(Float)
    Heavy_Atom_Count=Column(Float)
    Formal_Charge=Column(Float)
    Complexity=Column(Float)
    Isotope_Atom_Count=Column(Float)
    Undefined_Atom_Stereocenter_Count=Column(Float)
    Defined_Bond_Stereocenter_Count=Column(Float)
    Undefined_Bond_Stereocenter_Count=Column(Float)
    Covalently_Bonded_Unit_Count=Column(Float)
    Compound_Is_Canonicalized=Column(Boolean, default=True)
    Created_date=Column(DateTime, default= datetime.datetime.utcnow)
    results = relationship("Result",back_populates="molecules") # mise en place de la clé étrnagère dans la table result : result= nom de la table enfant et Molecules = le nom de la clé étrangère dans dans la table result

# la table Result
class Result(Base):
    __tablename__ ='results'
    id=Column(Integer,primary_key=True)
    Toxicity_Type=Column(String)
    value=Column(String) # pas sûr que ce soit string mais plutôt text
    CAS_Number=Column(String,ForeignKey("molecules.Numero_CAS")) #  la clé étrangère
    molecules = relationship("Molecule",back_populates="results") # mapping de la clé étrangère venant de la table molécule
    references=relationship("Reference" , secondary="referencements", back_populates="results")


# table Reference
class Reference(Base):
    __tablename__ ='references'
    id=Column(Integer,primary_key=True)
    number=Column(Integer)
    value=Column(String) # pas sûr que ce soit string mais plutôt text
    results=relationship("Result", secondary="referencements", back_populates="references")

# table Référencement

referencements = Table('referencements', Base.metadata,
    Column('result_id', ForeignKey('resultats.id'), primary_key=True),
    Column('reference_id', ForeignKey('references.id'), primary_key=True)
)
# Create the tables in the database
#Base.metadata.create_all(engine)