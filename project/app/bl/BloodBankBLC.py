from itertools import count
from project.app.repositories.BloodBankRepository import BloodBankRepository
from http import HTTPStatus
from project.app.db import db
from flask import request, jsonify


class BloodBankBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def adding_bloodbank(args):
        session = BloodBankBLC.get_session()
        res = BloodBankRepository.add_bb_todb(session, args)
        return res

    @staticmethod
    def get_single_bb(args):
        session = BloodBankBLC.get_session()
        res = BloodBankRepository.get_single_bb_byid(session, args)
        return res

    @staticmethod
    def updating_bloodbank(args):
        session = BloodBankBLC.get_session()
        bk = BloodBankRepository.get_single_bb_byid(session, args)
        if bk:
            res = BloodBankRepository.update_bb_todb(session, args, bk)
            return res

    @staticmethod
    def get_all_bb():
        session = BloodBankBLC.get_session()
        res = BloodBankRepository.getting_all_bb(session)
        return res

    @staticmethod
    def delete_bloodbank(args):
        session = BloodBankBLC.get_session()
        bb = BloodBankRepository.get_single_bb_byid(session, args)
        if not bb:
            return (
                jsonify({"message": "bloodbank not found"}),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        session.delete(bb)
        session.commit()
        return jsonify(
            {"message": f"bloodbank{args.get('BloodBankID')} is deleted successfully"}
        )

    @staticmethod
    def get_availble_bloods(args):
        session = BloodBankBLC.get_session()
        res = BloodBankRepository.geting_available_bloods(session, args)

        if res:
            return res

    @staticmethod
    def gets_all_availble_bloods():
        session = BloodBankBLC.get_session()
        res = BloodBankRepository.getting_all_availble_bloods(session)
        if res:
            ans = []
            for bank in res:
                avail = {}
                for donor in bank.blooddonations:
                    bloodtype = donor.BloodType
                    if bloodtype in avail:
                        avail[bloodtype] += 1
                    else:
                        avail[bloodtype] = 1

                bank_info = {
                    "BloodBankName": bank.BloodBankName,
                    "ContactNumber": bank.ContactNumber,
                    "Location": bank.Location,
                    "BloodType": [
                        {"Type": blood, "TotalAvailable": count}
                        for blood, count in avail.items()
                    ],
                }
                ans.append(bank_info)

            return ans
