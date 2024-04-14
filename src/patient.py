from uuid import uuid4
from datetime import datetime
from config import config
from db_config import db_config

class Patient:
    def __init__(self, name, gender, age):
        self.id = str(uuid4())
        self.name = name
        self.gender = gender
        self.age = age
        self.checkin = datetime.now().strftime(config['date_time_format'])
        self.checkout = None
        self.ward = None
        self.room = None

    def update_room_and_ward(self, ward, room):
        if ward not in db_config['wards']:
            raise ValueError("Invalid ward")

        if room not in db_config['rooms_per_ward']:
            raise ValueError("Invalid room")

        self.ward = ward
        self.room = room

    def commit_to_database(self, api_controller):
        patient_data = {
            'patient_id': self.id,
            'patient_name': self.name,
            'patient_age': self.age,
            'patient_gender': self.gender,
            'patient_checkin': self.checkin,
            'patient_checkout': self.checkout,
            'patient_ward': self.ward,
            'patient_room': self.room
        }

        response, status_code = api_controller.create_patient(patient_data)
        if status_code == 200:
            print("Patient successfully committed to the database.")
        else:
            print("Failed to commit patient to the database:", response)



