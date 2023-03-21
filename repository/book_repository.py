from sqlite3 import Connection
from model.book import Book

class BookRepository():
    def __init__(self, db: Connection) -> None:
        self.db =  db
        
    def insert(self, book: Book):
        self.db.execute(
            f"""
                INSERT INTO book (name, country, born) VALUES
                    (
                        '{book.name}', 
                        '{book.country}', 
                        '{book.born}'
                    );
            """
        )
        self.db.commit()

    def update(self, id: int, book: Book):
        self.db.execute(
            f"""
            UPDATE book
            SET 
                name = '{book.name}', 
                country = '{book.country}', 
                born = '{book.born}'
            WHERE id = {id};
            """
        )
        self.db.commit()

    def find_by_name(self, name: str) -> list[Book]:
        cursor = self.db.cursor()
        cursor.execute(f"select * from book where name like '%{name}%'")
        result = cursor.fetchall()

        def to_book(tuple):
            return Book.with_id(tuple[0], tuple[1], tuple[2], tuple[3])

        return list(map(to_book, result))
    
    def get_by_id(self, id):
        cursor = self.db.cursor()
        cursor.execute(f"select * from book where id = {id}")
        result = cursor.fetchone()
        return Book.with_id(result[0], result[1], result[2], result[3])

    def delete(self, id):
        self.db.execute(
            f"""
            DELETE FROM book
            WHERE id = {id};
            """
        )
        self.db.commit() 

    def get_list(self):
        cursor = self.db.cursor()
        cursor.execute(f"select * from book")
        result = cursor.fetchall()

        def to_book(tuple):
            return Book.with_id(tuple[0], tuple[1], tuple[2], tuple[3])

        return list(map(to_book, result))