from sqlalchemy import desc
from project.app.db import db
from project.app.models.Staff import Staff
from project.app.models.Registeration import Registeration
from werkzeug.security import generate_password_hash


class StaffRepository:
    @staticmethod
    def creating_staff(args, session):
        staff = Staff(**args)
        session.add(staff)
        session.commit()
        result = (
            session.query(Staff)
            .filter(Staff.FirstName == args.get("FirstName"))
            .order_by(desc(Staff.StaffID))
            .first()
        )
        return result

    @staticmethod
    def get_single_staff_id(args, session):
        result = (
            session.query(Staff).filter(Staff.StaffID == args.get("StaffID")).first()
        )
        return result

    @staticmethod
    def getting_all_staffs(session):
        res = session.query(Staff).all()
        return res

    @staticmethod
    def updating_the_staff(args, session, staff):
        staff.FirstName = args.get("FirstName")
        staff.LastName = args.get("LastName")
        staff.Email = args.get("Email")
        staff.Position = args.get("Position")
        staff.ContactNumber = args.get("ContactNumber")
        session.commit()
        result = (
            session.query(Staff).filter(Staff.StaffID == args.get("StaffID")).first()
        )
        return result

    @staticmethod
    def get_single_staff_byname(args, session):
        res = session.query(Staff).filter(Staff.Email == args.get("Email")).first()
        return res

    @staticmethod
    def registerated(args, session, staff):
        registeration = Registeration(**args)
        session.add(registeration)
        registeration.staffs.append(staff)
        session.commit()

    @staticmethod
    def get_registeration_by_email(args, session):
        res = (
            session.query(Registeration)
            .filter(Registeration.Email == args.get("Email"))
            .first()
        )
        return res

    @staticmethod
    def get_registeration_by_email_for_api(user, session):
        res = session.query(Registeration).filter(Registeration.Email == user).first()
        return res
