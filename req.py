import requests

requests.post('http://localhost:5000/patients', json={'name': 'Andy', 'age': 20, 'discharge_status': '0'})
requests.get('http://localhost:5000/patients').json()
requests.get('http://localhost:5000/patients/2').json()
requests.put('http://localhost:5000/patients/2', json={'name': 'Ko Khant', 'age': 20, 'discharge_status': '0'})
requests.delete('http://localhost:5000/patients/3')





