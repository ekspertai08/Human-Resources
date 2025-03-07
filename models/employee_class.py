import models.DB_class as db
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship 
import datetime

class Employee(db.Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    dob = Column(Date, nullable=False)
    position = Column(String(50), nullable=False)
    salary = Column(Integer, nullable=False)
    works_from = Column(Date, default=datetime.date.today())
    department_id = Column(Integer, ForeignKey("departments.id"))

    departments = relationship('Department', back_populates='managers')
    project_associations = relationship('Employee_Project', back_populates='employee')

    def __init__(self, name, last_name, dob, position, salary, department_id):
        self.name = name
        self.last_name = last_name
        self.dob = dob
        self.position = position
        self.salary = salary
        self.department_id = department_id
    
    def __str__(self):
        return f"{self.id} | {self.name} | {self.last_name} | {self.dob} | {self.position} | {self.salary} | {self.works_from} | {self.department_id}"
    
    def __repr__(self):
        return f"{self.id} | {self.name}"
