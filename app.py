from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/patient_db'  # PostgreSQL database connection
db = SQLAlchemy(app)

class Patient(db.Model):
    __tablename__ = 'ms_patient'
    msd_id = db.Column(db.Integer(), primary_key=True)
    msd_name = db.Column(db.String(150))  # New field for patient's name
    msd_age = db.Column(db.Integer())  # New field for patient's age
    msd_discharge_status = db.Column(db.String(1))  # New field for patient's discharge status

    def __repr__(self):
        return '<User %r>' % self.username

class PatientSchema(Schema):
    msd_id = fields.Int(data_key='patient_id')
    msd_name = fields.Str(data_key='name')  # New field for patient's name
    msd_age = fields.Int(data_key='age')  # New field for patient's age
    msd_discharge_status = fields.Str(data_key='discharge_status')  # New field for patient's discharge status

patient_schema = PatientSchema()

with app.app_context():
    db.create_all()

# Create - Add a new patient
@app.route('/patients', methods=['POST'])
def create_patient():
    data = request.get_json()
    patient = Patient(msd_name=data['name'], msd_age=data['age'], msd_discharge_status=data['discharge_status'])
    db.session.add(patient)
    db.session.commit()
    return patient_schema.dump(patient), 201

# Read - Get all patients
@app.route('/patients', methods=['GET'])
def get_all_patients():
    patients = Patient.query.all()
    return patient_schema.dump(patients, many=True)

# Read - Get a specific patient
@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if patient is None:
        return jsonify({'error': 'Patient not found'}), 404
    return patient_schema.dump(patient)

# Update - Modify a patient
@app.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if patient is None:
        return jsonify({'error': 'Patient not found'}), 404
    data = request.get_json()
    patient.msd_name = data['name']
    patient.msd_age = data['age']
    patient.msd_discharge_status = data['discharge_status']
    db.session.commit()
    return patient_schema.dump(patient), 200

# Delete - Remove a patient
@app.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if patient is None:
        return jsonify({'error': 'Patient not found'}), 404
    db.session.delete(patient)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
