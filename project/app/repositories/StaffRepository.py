from project.app.db import db
from project.app.models.Staff import Staff


class StaffRepository:
    @staticmethod
    def get_dept_name(session, department_name):
        result = session.query(Staff).filter(Staff.name == department_name).first()
        return result
