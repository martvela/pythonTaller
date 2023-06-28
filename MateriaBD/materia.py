class materia:
    #constructor
    def __init__(self,id,tittle):
        self.id=id
        self.tittle=tittle
    def __str__(self):
        return f'id = {self.id} titulo = {self.tittle}'