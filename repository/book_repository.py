from sqlite3 import Connection
from model.book import Book

class BookRepository():
    def __init__(self, db: Connection) -> None:
        self.db =  db