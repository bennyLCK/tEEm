import requests

requests.post('http://localhost:5000/todos', json={'task': 'Learn Flask'})
requests.get('http://localhost:5000/todos').json()
requests.get('http://localhost:5000/todos/1').json()
requests.put('http://localhost:5000/todos/1', json={'task': 'Master Flask'})
requests.delete('http://localhost:5000/todos/1')





