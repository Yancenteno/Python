from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Question:
    db = "rick_schema"
    def __init__(self, data) -> None:
        self.id = data['id']
        self.question = data['question']
        self.choice1 = data['choice1']
        self.choice2 = data['choice2']
        self.choice3 = data['choice3']
        self.choice4 = data['choice4']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']