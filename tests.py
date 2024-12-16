import pytest
from app import app, db
from models import Todo

@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/test_todo_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.create_all()
    yield app.test_client()
    db.drop_all()

def test_add_todo(client):
    response = client.post('/todos', json={'task': 'Test Task'})
    assert response.status_code == 201
    assert response.json['message'] == 'Task added successfully!'

def test_get_todos(client):
    client.post('/todos', json={'task': 'Test Task'})
    response = client.get('/todos')
    assert response.status_code == 200
    assert len(response.json) == 1

def test_update_todo(client):
    response = client.post('/todos', json={'task': 'Test Task'})
    todo_id = response.json['id']
    response = client.put(f'/todos/{todo_id}', json={'task': 'Updated Task', 'done': True})
    assert response.status_code == 200
    assert response.json['message'] == 'Task updated successfully!'

def test_delete_todo(client):
    response = client.post('/todos', json={'task': 'Test Task'})
    todo_id = response.json['id']
    response = client.delete(f'/todos/{todo_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Task deleted successfully!'

def test_delete_all_todos(client):
    client.post('/todos', json={'task': 'Test Task'})
    response = client.delete('/todos')
    assert response.status_code == 200
    assert response.json['message'] == 'All tasks deleted!'
