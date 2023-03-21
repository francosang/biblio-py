class Book():
    def __init__(self, name, year, genre) -> None:
        self.id = None
        self.name = name
        self.year = year
        self.genre = genre

    def with_id(id, name, year, genre):
        auth =  Book(name, year, genre)
        auth.id = id
        return auth
