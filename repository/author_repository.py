from sqlite3 import Connection
from model.author import Author

class AuthorRepository():
    def __init__(self, db: Connection) -> None:
        self.db =  db

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

    def find_by_name(self, name: str) -> list[Author]:
        cursor = self.db.cursor()
        cursor.execute(f"select * from author where name like '%{name}%'")
        result = cursor.fetchall()

        def to_author(tuple):
            return Author.with_id(tuple[0], tuple[1], tuple[2], tuple[3])

        return list(map(to_author, result))
    
    def get_by_id(self, id):
        cursor = self.db.cursor()
        cursor.execute(f"select * from author where id = {id}")
        result = cursor.fetchone()
        return Author.with_id(result[0], result[1], result[2], result[3])

    def delete(self, id):
        self.db.execute(
            f"""
            DELETE FROM author
            WHERE id = {id};
            """
        )
        self.db.commit() 

    def get_list(self):
        cursor = self.db.cursor()
        cursor.execute(f"select * from author")
        result = cursor.fetchall()

        def to_author(tuple):
            return Author.with_id(tuple[0], tuple[1], tuple[2], tuple[3])

        return list(map(to_author, result))