from sqlalchemy import Column, Integer, String,Float,ForeignKey,DateTime, Boolean, Table
from config import Base, engine
from sqlalchemy.orm import relationship
import datetime
# la table molecule

class Molecule(Base):
    __tablename__ = 'molecules'
    CAS_Number=Column(String(255),primary_key=True)
    Name=Column(String(255))
    Canonical_Formula=Column(String(255))
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
    Toxicity_Type=Column(String(255))
    value=Column(String(255)) # pas sûr que ce soit String(255) mais plutôt text
    CAS_Number=Column(String(255),ForeignKey("molecules.CAS_Number")) #  la clé étrangère
    Created_date=Column(DateTime, default= datetime.datetime.utcnow)
    molecules = relationship("Molecule",back_populates="results") # mapping de la clé étrangère venant de la table molécule
    references=relationship("Reference" , secondary="referencements", back_populates="results")


# table Reference
class Reference(Base):
    __tablename__ ='references'
    id=Column(Integer,primary_key=True)
    number=Column(Integer)
    Created_date=Column(DateTime, default= datetime.datetime.utcnow)
    value=Column(String(255)) # pas sûr que ce soit String(255) mais plutôt text
    results=relationship("Result", secondary="referencements", back_populates="references")

# table Référencement

referencements = Table('referencements', Base.metadata,
    Column('result_id', ForeignKey('results.id'), primary_key=True),
    Column('reference_id', ForeignKey('references.id'), primary_key=True)
)

class User(Base):
    __tablename__="users"
    Firstname = Column(String(255))
    Lastname =Column(String(255))
    Email = Column(String(255),primary_key=True)
    Password =Column(String(255))
    Created_at=Column(DateTime, default= datetime.datetime.utcnow)

# class Resultat(Base):
    # __tablename__ ='resultats'
    # id=Column(Integer,primary_key=True)
    # Toxicity_Type=Column(String(255))
    # value=Column(String(255)) # pas sûr que ce soit String(255) mais plutôt text
    # CAS_Number=Column(String(255))
# Create the tables in the database
Base.metadata.create_all(engine)

