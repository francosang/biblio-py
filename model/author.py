class Author():

    def __init__(self, name, country, born) -> None:
        self.id = None
        self.name = name
        self.country = country
        self.born = born
    
    def build(tuple):
        auth =  Author(tuple[1], tuple[2], tuple[3])
        auth.id = tuple[0]
        return auth
