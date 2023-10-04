# banco de dados
import re
from app import mongo

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
class Nota:
    def __init__(self, aluno_id, nota_p1, nota_p2, listas_string):
        self.aluno_id = aluno_id
        self.nota_p1 = nota_p1
        self.nota_p2 = nota_p2
        self.listas_raw = listas_string     #Foi definido que receberíamos as listas como notas sucessivas separadas por '+'
        self.listas = []
        self.definir_media_listas()
        self.definir_media_parcial()

    def definir_media_listas(self):
        partes = re.split(r'\s*\+\s*', self.listas_raw)

        numbers = [float(parte) for parte in partes if parte.isdigit()]
        self.media_listas = sum(numbers)/len(numbers)

    def definir_media_parcial(self):
        self.media_parcial = (self.nota_p1 + self.nota_p2)*0.8 + (self.media_listas)*0.2
        if self.media_parcial >= 7:
            self.situaco = 'Aprovado'
        elif self.media_parcial < 7 and self.media_parcial >= 3:
            self.situacao = 'Prova Final'
        else:
            self.situacao = 'Reprovado'