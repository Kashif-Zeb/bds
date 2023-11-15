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
            .first()
        )
        return res
