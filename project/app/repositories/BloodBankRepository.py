from sqlalchemy import func
from project.app.models.BloodBank import BloodBank

from project.app.db import db
from project.app.models.BloodDonation import BloodDonation


class BloodBankRepository:
    @staticmethod
    def add_bb_todb(session, args):
        result = BloodBank(**args)
        session.add(result)
        session.commit()
        res = (
            session.query(BloodBank)
            .filter(BloodBank.BloodBankName == args.get("BloodBankName"))
            .first()
        )
        return res

    @staticmethod
    def get_single_bb_byid(session, args):
        res = (
            session.query(BloodBank)
            .filter(BloodBank.BloodBankID == args.get("BloodBankID"))
            .first()
        )
        return res

    staticmethod

    def update_bb_todb(session, args, bk):
        bk.BloodBankName = args.get("BloodBankName")
        bk.Location = args.get("Location")
        bk.Email = args.get("Email")
        bk.ContactNumber = args.get("ContactNumber")
        session.commit()
        res = (
            session.query(BloodBank)
            .filter(BloodBank.BloodBankID == args.get("BloodBankID"))
            .first()
        )
        return res

    @staticmethod
    def getting_all_bb(session):
        res = session.query(BloodBank).all()
        return res

    @staticmethod
    def geting_available_bloods(session, args):
        # breakpoint()
        # res = (
        #     session.query(BloodBank)
        #     .filter(BloodBank.BloodBankName == args.get("BloodBankName"))
        #     .first()
        # )
        # # bd = res.blooddonations
        # # main = (
        # #     session.query(res.blooddonations.BloodType, func.count(res.blooddonations.DonationID))
        # #     .group_by(res.blooddonations.BloodType)
        # #     .all()
        # # )
        # main = (
        #     session.query(BloodDonation.BloodType, func.count(BloodDonation.DonationID))
        #     .group_by(BloodDonation.BloodType)
        #     .all()
        # )
        # ans = [
        #     {
        #         "BloodBankName": res.BloodBankName,
        #         "ContactNumber": res.ContactNumber,
        #         "Location": res.Location,
        #         "BloodType": [
        #             {
        #                 "Type": blood,
        #                 "TotalAvailable": count,
        #             }
        #             for blood, count in main
        #         ],
        #     }
        # ]
        # # if main:
        # #     ans = {
        # #         "BloodBankName": res.BloodBankName,
        # #         "BloodType": [
        # #             {
        # #                 "Type": blood,
        # #                 "TotalAvailable": count,
        # #             }
        # #             for blood, count in main
        # #         ],
        # #     }
        # # else:
        # #     ans = "No data available"
        # return ans
        res = (
            session.query(BloodBank)
            .filter(BloodBank.BloodBankName == args.get("BloodBankName"))
            .first()
        )

        if res:
            blood_types_count = {}
            for donation in res.blooddonations:
                blood_type = donation.BloodType
                if blood_type in blood_types_count:
                    blood_types_count[blood_type] += 1
                else:
                    blood_types_count[blood_type] = 1

                ans = [
                    {
                        "BloodBankName": res.BloodBankName,
                        "ContactNumber": res.ContactNumber,
                        "Location": res.Location,
                        "BloodType": [
                            {"Type": blood, "TotalAvailable": count}
                            for blood, count in blood_types_count.items()
                        ],
                    }
                ]
            return ans
        else:
            return "Blood bank not found"

    @staticmethod
    def getting_all_availble_bloods(session):
        res = session.query(BloodBank).all()
        return res
