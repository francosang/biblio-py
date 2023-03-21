from sqlite3 import Connection
from model.author import Author

class AuthorRepository():
    def __init__(self, db: Connection) -> None:
        self.db = db
        
    def insert(self, author: Author):
        self.db.execute(
            f"""
                INSERT INTO author (name, country, born) VALUES
                    (
                        '{author.name}', 
                        '{author.country}', 
                        '{author.born}'
                    );
            """
        )
        self.db.commit()

    def update(self, id: int, author: Author):
        self.db.execute(
            f"""
            UPDATE author
            SET 
                name = '{author.name}', 
                country = '{author.country}', 
                born = '{author.born}'
            WHERE id = {id};
            """
        )
        self.db.commit()

    def delete(self, id):
        self.db.execute(
            f"""
            DELETE FROM author
            WHERE id = {id};
            """
        )
        self.db.commit() 

    def find_by_name(self, name: str) -> list[Author]:
        try:
            cursor = self.db.cursor()
            cursor.execute(f"select * from author where name like '%{name}%'")
            result = cursor.fetchall()
            return list(map(Author.build, result))
        finally:
            cursor.close()
    
    def get_by_id(self, id):
        try:
            cursor = self.db.cursor()
            cursor.execute(f"select * from author where id = {id}")
            result = cursor.fetchone()
            return Author.build(result)
        finally:
            cursor.close()

    def get_list(self):
        try:
            cursor = self.db.cursor()
            cursor.execute(f"select * from author")
            result = cursor.fetchall()
            return list(map(Author.build, result))
        finally:
            cursor.close()
