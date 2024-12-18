#models needed here are 2 the Bank branch model and Account model
#
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, declarative_base

Base =declarative_base()
 
class Branch(Base):
    __tablename__ ="Branch"
    id = Column(Integer, primary_key=True)
    name= Column(String,nullable=false)
    location= Column(String, nullable=false)

    accounts= relationship("BankAccounts", back_populates="branch", cascade="all")
    def __repr__(self):
        return f"Branch(id= {self.id} name ={self.name} location={self.location})"


class BankAccounts(Base):
    __tablename__ ="BankAccounts"
    id = Column(Integer, primary_key=True)
    holdersname= Column(String,nullable=false)
    balance = Column(Float, default=0.0)
    branch_id = Column(Integer, ForeignKey("Branch.id"))
    
    branch = relationship("Branch", back_populates="BankAccounts")

    def __repr__(self):
        return f"BankAccount(id={self.id}, name{self.holdersname},branch={self.branch} branchid{self.branch_id})"