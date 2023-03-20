from repository.author_repository import AuthorRepository
import sqlite3

__DBNAME__ = None

if not __DBNAME__:
    __DBNAME__ = "biblo.db"
else:
    raise RuntimeError("Database name has already been set.")

con = sqlite3.connect(__DBNAME__)
author_repository = AuthorRepository(con)