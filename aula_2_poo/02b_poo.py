class Balde:
    """Essa classe modela os objetos"""

    def __init__(self):

        # atributos simples
        self.marca = ""
        self.durabilidade_em_anos = 0
        self.volume = ""
        self.material = ""


    def __str__(self):
        return self.marca
#
#     def __repr__(self):
#         return self.marca

# instanciamento
castelo_1 = Balde()
castelo_2 = Balde()

print(castelo_1)
print(castelo_2)
