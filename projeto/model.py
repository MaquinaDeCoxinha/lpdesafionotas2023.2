# banco de dados
from projeto import mongo

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
class Nota:
    def __init__(self, nota_p1, nota_p2):
        self.nota_p1 = nota_p1
        self.nota_p2 = nota_p2
        self.listas = []
        self.medialistas
        self.mediafinal