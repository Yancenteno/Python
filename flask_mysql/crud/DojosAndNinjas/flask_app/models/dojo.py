from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
    @classmethod
    def save(cls, data):
        query = """
        Insert INTO dojos (name, created_at, updated_at)
        VALUES (%(name)s, NOW(), NOW());
        """
        dojo_id = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return dojo_id
    
    @classmethod
    def get_all(cls):
        query = """
        SELECT * 
        FROM dojos;
        """
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        all_dojos = []
        for d in result:
            all_dojos.append(cls(d))
        return all_dojos
    
    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM dojos
        WHERE dojos.id = %(id)s;
        """
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def update(cls, data):
        query = """
        UPDATE dojos SET name = %(name)s, updated_at = NOW()
        WHERE id = %(id)s;
        """
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    @classmethod
    def get_dojo_ninjas(cls, data):
        query = """
        SELECT * FROM dojos
        JOIN ninjas ON ninjas.dojo_id = dojos.id
        WHERE dojos.id = %(id)s;
        """
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print(result)
        dojos = []
        for r in result:
            dojos.append(cls(r))
            # dojos.ninjas.append(ninja.Ninja())
        return dojos
    