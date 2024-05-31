from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema

db = SQLAlchemy()

class Patient(db.Model):
    __tablename__ = 'ms_patient'
    msd_id = db.Column(db.Integer(), primary_key=True)
    msd_name = db.Column(db.String(150))  # New field for patient's name
    msd_age = db.Column(db.Integer())  # New field for patient's age
    msd_discharge_status = db.Column(db.String(1))  # New field for patient's discharge status


class PatientSchema(Schema):
    msd_id = fields.Int(data_key='patient_id')
    msd_name = fields.Str(data_key='name')  # New field for patient's name
    msd_age = fields.Int(data_key='age')  # New field for patient's age
    msd_discharge_status = fields.Str(data_key='discharge_status')  # New field for patient's discharge status