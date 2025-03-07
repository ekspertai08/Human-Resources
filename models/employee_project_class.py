import models.DB_class as db
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String, Date, ForeignKey

class Employee_Project(db.Base):
    __tablename__ = 'employees_projects'
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))

    employee = relationship('Employee', back_populates='project_associations')
    project = relationship('Project', back_populates='employee_associations')
