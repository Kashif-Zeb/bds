from http import HTTPStatus
from flask import jsonify
from sqlalchemy import desc
from project.app.models.BloodDonation import BloodDonation
from project.app.db import db


class BloodDonationRepository:
    @staticmethod
    def adding_blooddonation(args, session, donor):
        args.pop("DonorID")
        # args.pop("BloodBankID")
        blooddonation = BloodDonation(**args)
        blooddonation.donors.append(donor)
        # blooddonation.bloodbanks.append(bloodbank)
        session.add(blooddonation)
        session.commit()
        bloodD = (
            session.query(BloodDonation)
            .filter(BloodDonation.DonationDate == args.get("DonationDate"))
            .order_by(desc(BloodDonation.DonationID))
            .first()
        )
        return bloodD

    @staticmethod
    def get_blooddonation_byid(args, sesssion):
        res = (
            sesssion.query(BloodDonation)
            .filter(BloodDonation.DonationID == args.get("DonationID"))
            .first()
        )
        return res

    @staticmethod
    def getting_all_the_blooddonations(session):
        res = session.query(BloodDonation).all()
        return res

    @staticmethod
    def updating_the_blooddonation(args, session, blooddonation):
        blooddonation.DonationDate = (args.get("DonationDate"),)
        blooddonation.BloodType = (args.get("BloodType"),)
        blooddonation.DonationStatus = (args.get("DonationStatus"),)
        blooddonation.HemoglobinLevel = args.get("HemoglobinLevel")
        session.commit()
        res = (
            session.query(BloodDonation)
            .filter(BloodDonation.DonationID == blooddonation.DonationID)
            .first()
        )
        return res

    @staticmethod
    def update_the_status(args, session, bloodbank):
        res = (
            session.query(BloodDonation)
            .filter(BloodDonation.DonationID.in_(args.get("DonationID")))
            .all()
        )
        ids = [i.DonationID for i in res]
        not_found = list(set(args.get("DonationID")).symmetric_difference(ids))
        if not_found:
            return (
                jsonify({"error": f"donation ids: {not_found} not found!]"}),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        else:
            for i in res:
                i.DonationStatus = args.get("DonationStatus")
                # session.commit()
                if i.DonationStatus == "Approved":
                    i.bloodbanks.append(bloodbank)
            try:
                session.commit()
            except:
                session.rollback()
            return {"message": "Donation status updated "}, HTTPStatus.OK

    @staticmethod
    def getting_search_status(args, session):
        res = (
            session.query(BloodDonation)
            .filter(BloodDonation.DonationStatus == args.get("DonationStatus"))
            .all()
        )
        return res
