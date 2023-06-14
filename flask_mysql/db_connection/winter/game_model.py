from mysqlconnection import connectToMySQL


class Game:
    DB = 'game_db'
    
    
    def __init__(self, data):
        self.id = data['id']
        self.name=data['name']
        self.genre=data['genre']
        self.release_year=data['release_year']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']


    @classmethod
    def get_all(cls):
        query=""" 
        SELECT * 
        FROM games;
        """
        
        results = connectToMySQL(cls.DB).query_db(query)
        
        all_games= []
        
        
        for game in results:
            all_games.append( cls(game) )
        
        return all_games
    
    @classmethod
    def add_games(cls, data):
        query = """
        INSERT INTO games (name, genre, release_year)
        Values( %(name)s, %(genre)s, %(release_year)s  )
        """
        
        results = connectToMySQL(cls.DB).query_db(query, data)
        
        return results
    
    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM games
        WHERE id = %(game_id)s;
        """
        
        results = connectToMySQL(cls,DB).query_db(query, data)
        
        return cls(results[0])