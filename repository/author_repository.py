from sqlite3 import Connection
from model.author import Author

class AuthorRepository():
    def __init__(self, db: Connection) -> None:
        self.db =  db

    def save(self, author: Author):
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

    def findByName(self, name: str) -> list[Author]:
        cursor = self.db.cursor()
        cursor.execute(f"select * from author where name like '%{name}%'")
        result = cursor.fetchall()

        def to_author(tuple):
            return Author(tuple[1], tuple[2], tuple[3])

        return list(map(to_author, result))