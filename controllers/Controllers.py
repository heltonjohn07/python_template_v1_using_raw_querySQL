
from database.conn_db import *
from models.models import People

people = Table('people')

def controller_get_people():
    sql = Query.from_(people).select('*')
    r = select_db(sql)
    return r

def controller_get_people_id(id: int):
    sql = Query.from_(people).select('*').where(people.id==id)
    r = select_db(sql)
    return r

def controller_create_people(person: People):
    sql = Query.into(people) \
    .columns('name') \
    .insert(person.name)
    
    query_db(sql)


def controller_update_people(id: int, person:People):
    
    sql = Query.from_(people).select('id').where(people.id==id)
    id = select_db(sql)

    if(id==[]):
        return {'error':"id não existe"}

    id = id[0][0]
    
    sql = Query.update(people).set(people.name, person.name ).where(people.id == id)
    query_db(sql)

    sql = Query.from_(people).select('*').where(people.id == id)
    r = select_db(sql)

    return(r[0])

def controller_delete_people(id: int):
    
    sql = Query.from_(people).select('id').where(people.id==id)
    id = select_db(sql)

    if(id==[]):
        return {'error':"id não existe"}

    id = id[0][0]
    
    sql = Query.from_(people).delete().where(people.id == id)
    query_db(sql)

    return{'status':204}
