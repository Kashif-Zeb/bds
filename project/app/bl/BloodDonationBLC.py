from project.app.repositories.BloodDonationRepository import BloodDonationRepository
from project.app.db import db
from flask import request, jsonify
from project.app.repositories.DonorRepository import DonorRepository


class BloodDonationBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def creating_blooddonation(args):
        session = BloodDonationBLC.get_session()

        donor = DonorRepository.get_single_donor_byid(args, session)
        # breakpoint()
        if donor:
            donorID = args.get("DonorID")
            blooddonation = BloodDonationRepository.adding_blooddonation(
                args, session, donor
            )
            # blooddonation.donors.append(donor)
            # breakpoint()
            blooddonation.DonorID = donorID
            # blooddonation(args.get("DonorID"))

            return blooddonation

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
        res = BloodDonationRepository.update_the_status(args, session)
        return res
