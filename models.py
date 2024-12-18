from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Branch(Base):
    __tablename__ = "Branch"  
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    
    accounts = relationship("BankAccount", back_populates="branch", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Branch(id={self.id}, name={self.name}, location={self.location})"


class BankAccount(Base):
    __tablename__ = "BankAccounts"  
    id = Column(Integer, primary_key=True)
    holdersname = Column(String, nullable=False)
    balance = Column(Float, default=0.0)

    
    branch_id = Column(Integer, ForeignKey("Branch.id"), nullable=False)

   
    branch = relationship("Branch", back_populates="accounts")

    def __repr__(self):
        return f"BankAccount(id={self.id}, holdersname={self.holdersname}, balance={self.balance}, branch={self.branch})"
