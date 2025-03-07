import models.DB_class as db
import models.employee_class as ec
import models.project_class as pc
from sqlalchemy import Column, Integer, String, Date, ForeignKey

class Employee_Project(db.Base):
    __tablename__ = 'employees_projects'
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey(ec.employees.id))
    project_id = Column(Integer, ForeignKey(pc.projects.id))

db.Base.metadata.create_all(db.engine)