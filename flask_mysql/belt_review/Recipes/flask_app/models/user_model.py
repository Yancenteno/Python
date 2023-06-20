from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class User:
    db = "recipe_share"
    def __init__(self, data) -> None:
        self. id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        results = connectToMySQL(cls.db).query_db(query,data)
        return results
    
    @classmethod
    def get_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @staticmethod
    def validate_account(new_account):
        is_valid = True
        if len(new_account['first_name']) < 3:
            flash('First name must be 3 characters or more!')
            is_valid = False
        if len(new_account['last_name']) < 3:
            flash('Last name must be 3 characters or more!')
            is_valid = False
        if not EMAIL_REGEX.match(new_account['email']):
            flash('Please enter a valid email!')
            is_valid = False
        if len(new_account['password']) < 4:
            flash('Password must be 4 or more characters long!')
            is_valid = False
        if new_account['password'] != new_account['confirm_password']:
            is_valid = False
            flash('Passwords did not match!')
        
        return is_valid