class Author():

    def __init__(self, name, country, born) -> None:
        self.id = None
        self.name = name
        self.country = country
        self.born = born

    def with_id(id, name, country, born):
        auth =  Author(name, country, born)
        auth.id = id
        return auth
