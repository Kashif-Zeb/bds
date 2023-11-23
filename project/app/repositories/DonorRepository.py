from sqlalchemy import desc
from project.app.db import db

from project.app.models.Donor import Donor
from sqlalchemy.orm import joinedload

import datetime


class DonorRepository:
    @staticmethod
    def get_course_name(session, course_name):
        result = session.query(Donor).filter(Donor.name == course_name).first()
        return result

    @staticmethod
    def adding_donor(session, args):
        donor = Donor(**args)
        session.add(donor)
        session.commit()
        res = (
            session.query(Donor)
            .filter(Donor.FirstName == args.get("FirstName"))
            .order_by(
                desc(Donor.DonorID)
            )  # Replace 'column_name' with the column you want to order by
            .first()
        )
        return res

    @staticmethod
    def get_single_donor_byid(args, session):
        res = session.query(Donor).filter(Donor.DonorID == args.get("DonorID")).first()
        return res

    @staticmethod
    def update_donor_byid(exist, args, session):
        exist.FirstName = args.get("FirstName")
        exist.LastName = args.get("LastName")
        exist.Email = args.get("Email")
        exist.ContactNumber = args.get("ContactNumber")
        exist.Address = args.get("Address")
        exist.BloodType = args.get("BloodType")
        exist.DateOfBirth = args.get("DateOfBirth")
        exist.Gender = args.get("Gender")

        session.commit()
        res = session.query(Donor).filter(Donor.DonorID == exist.DonorID).first()
        return res

    @staticmethod
    def get_all_donors(session):
        res = session.query(Donor).all()
        return res

    @staticmethod
    def delete_donor_byid(args, session=db.session):
        # breakpoint()
        res = session.query(Donor).filter(Donor.DonorID == args.get("DonorID")).first()
        if res:
            session.delete(res)
            session.commit()
        else:
            raise Exception("No record found.")
