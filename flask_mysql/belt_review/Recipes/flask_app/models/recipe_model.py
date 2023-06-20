from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user_model

class Recipe:
    db = "recipe_share"
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under_30= data['under_30']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipe_poster = None
        
        
        
    @classmethod
    def save_recipe(cls, data):
        query = """
        INSERT INTO recipes(name, description, instructions, date, under_30, user_id) 
        VALUES(%(name)s, %(description)s, %(instructions)s, %(date)s, %(under_30)s, %(user_id)s);
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        return results
    
    
    
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(cls.db).query_db(query)
        all_recipes = []
        for row in results:
            user_data = {
                'id' : row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at']
            }
            one_recipe = cls(row)
            one_recipe.recipe_poster = user_model.User(user_data)
            all_recipes.append(one_recipe)
        return all_recipes
    
    
    
    @classmethod
    def get_one_recipe(cls, data):
        query = """
        SELECT * FROM recipes 
        JOIN users ON users.id = recipes.user_id 
        WHERE recipes.id = %(recipe_id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        one_recipe = cls(results[0])
        user_data = {
                'id' : results[0]['users.id'],
                'first_name' : results[0]['first_name'],
                'last_name' : results[0]['last_name'],
                'email' : results[0]['email'],
                'password' : results[0]['password'],
                'created_at' : results[0]['users.created_at'],
                'updated_at' : results[0]['users.updated_at']
            }
        one_recipe.recipe_poster = user_model.User(user_data)
        
        return one_recipe
    
    
    
    @classmethod
    def update_recipe(cls, data):
        query = """
        UPDATE recipes
        SET name = %(name)s,
        description = %(description)s,
        instructions = %(instructions)s,
        date = %(date)s,
        under_30 = %(under_30)s
        WHERE id = %(recipe_id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    
    
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(recipe_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    
    
    @staticmethod
    def validate_recipe(new_recipe):
        is_valid = True
        if len(new_recipe['name']) < 1:
            flash('Name field is required!')
            is_valid = False
        if len(new_recipe['description']) < 1:
            flash('Description field is required!')
            is_valid = False
        if len(new_recipe['instructions']) < 1:
            flash('Instructions field is required!')
            is_valid = False
        if len(new_recipe['date']) < 1:
            flash('Date field is required!')
            is_valid = False
        if 'under_30' not in new_recipe:
            flash("Choose whether recipe is under 30 minutes!")
            is_valid = False
        return is_valid