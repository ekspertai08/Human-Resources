import models.DB_class as db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, ForeignKey

class Project(db.Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(100), nullable=False)

    employee_associations = relationship('Employee_Project', back_populates='project')

    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f"{self.id} | {self.name} | {self.description}"
    
    def __repr__(self):
        return f"{self.name}"
