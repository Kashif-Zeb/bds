from project.app.repositories.BloodDonationRepository import BloodDonationRepository
from project.app.db import db
from flask import request, jsonify
from project.app.repositories.DonorRepository import DonorRepository
from project.app.repositories.BloodBankRepository import BloodBankRepository


class BloodDonationBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def creating_blooddonation(args):
        session = BloodDonationBLC.get_session()
        # bloodbank = BloodBankRepository.get_single_bb_byid(session, args)
        donor = DonorRepository.get_single_donor_byid(args, session)
        # breakpoint()
        # if bloodbank:
        if donor:
            donorID = args.get("DonorID")
            # bloodbankID = args.get("BloodBankID")
            blooddonation = BloodDonationRepository.adding_blooddonation(
                args, session, donor
            )
            # blooddonation.donors.append(donor)
            # breakpoint()
            blooddonation.DonorID = donorID
            # blooddonation.BloodBankID = bloodbankID
            # blooddonation(args.get("DonorID"))
            return blooddonation
        raise ("first provide the donor info")
        # raise ("bloodbank not found")

    @staticmethod
    def getting_blooddonation(args):
        sesssion = BloodDonationBLC.get_session()
        blooddonations = BloodDonationRepository.get_blooddonation_byid(args, sesssion)
        return blooddonations

    @staticmethod
    def getting_all_blooddonations():
        session = BloodDonationBLC.get_session()
        blooddonations = BloodDonationRepository.getting_all_the_blooddonations(session)
        return blooddonations

    @staticmethod
    def updating_blooddonation(args):
        session = BloodDonationBLC.get_session()

        blooddonation = BloodDonationRepository.get_blooddonation_byid(args, session)
        if blooddonation:
            res = BloodDonationRepository.updating_the_blooddonation(
                args, session, blooddonation
            )
            return res

    @staticmethod
    def updating_donationstatus(args):
        session = BloodDonationBLC.get_session()
        bloodbank = BloodBankRepository.get_single_bb_byid(session, args)
        res = BloodDonationRepository.update_the_status(args, session, bloodbank)
        return res

    @staticmethod
    def get_search_status(args):
        session = BloodDonationBLC.get_session()
        status = BloodDonationRepository.getting_search_status(args, session)
        return status
