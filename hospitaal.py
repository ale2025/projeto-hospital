class Pessoa:

    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def imprimir_dados(self):

        print('Nome: ' + self.nome) 
        print('Idade: '+ self.idade)
        print('Genero: ' + self.genero)

class Paciente(Pessoa):
    def __init__(self, sintoma, nome, idade, genero):  
        super().__init__(nome, idade, genero)
        self.sintoma = sintoma

    def imprimir_sintoma(self):
        return print('Sintomas: ' + self.sintoma)

class Medico(Pessoa):
    def __init__(self, crm, nome, idade, genero):
        super().__init__(nome, idade, genero)
        self.crm = crm

    def imprimir_crm(self):

        return print( 'CRM: ' + self.crm)

print('________PACIENTE_______')

paciente = Paciente('Gripe', 'Marcia', '23', 'F')
paciente.imprimir_dados()
paciente.imprimir_sintoma()

print('_________MEDICO______')

medico =  Medico('1234', 'Alexandre', '45', 'M')
medico.imprimir_crm()
medico.imprimir_dados()