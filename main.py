
from fastapi import FastAPI
from pypika import *

# from .database.conn_db import *
from models.models import People
from controllers.Controllers import *

app = FastAPI()
authors = Table('people')

#models
print('Server Running......')

#Rota Raiz
@app.get('/v1')
def index():
    return {"Welcome": "To API v1.0"}

@app.post('/v1/people', response_model = People)
def create_people(author: People):
    return controller_create_people(author)
    
@app.get('/v1/people')
def get_all_people():
    return controller_get_people()

@app.get('/v1/people/{id}')
def get_people_by_id(id: int):
    return controller_get_people_id(id)

@app.put('/v1/people/{id}')
def update_people_by_id(id: int, author:People):
    return controller_update_people(id, author)

@app.delete('/v1/people/{id}')
def delete_people_by_id(id: int):
    return controller_delete_people(id)
    
    


