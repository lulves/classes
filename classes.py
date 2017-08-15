class Pessoa ():
    nome = ''
    idade = None
    nacionalidade = ''
    
    def __init__ (self, nome="", idade=None, nacionalidade=""):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade
        
    def __str__ (self):
        return u'{} - {} - {} '.format(self.nome, self.idade, self.nacionalidade)
    
class PessoaFisica (Pessoa):
    cpf = None

    def __init__ (self, nome="", idade=None, nacionalidade="", cpf=None):
        Pessoa.__init__ (self, nome, idade, nacionalidade)
        self.cpf = cpf
    def __str__(self):
        return u'{} - {} - {} - {}'.format(self.nome, self.idade, self.nacionalidade, self.cpf)
    def executa (self):
        self.nome.ExecutaTarefa()

class PessoaJuridica(Pessoa):
    cnpj = None
    def __init__(self,nome="", idade=None, nacionalidade="", cnpj=None):
        Pessoa.__init__ (self, nome, idade, nacionalidade)
        self.cnpj= cnpj
    def __str__ (self):
        return u'{} - {} - {} - {}'.format(self.nome, self.idade, self.nacionalidade, self.cnpj)
    def AtribuiTarefa (self):
        self.nome.AtribuiTarefa()

class Projeto ():
    nome = ''
    objetivo =''
    def __init__ (self, nome='', obejetivo=''):
        self.nome=nome
        self.objetivo=objetivo
    def tarefas(self):
        self.nome.Pertence()
        
class Tarefa ():
    descricao = ""
    dataInicio = None
    dataFim = None
    prioridade = None
    def __init__ (self, descricao="", dataInicio=None, dataFim=None, prioridade=None):
        self.descricao = descricao
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.prioridade = prioridade

    def AtribuiTarefa (self):
        print("%s atrubuiu a tarefa" %self.nome)

    def ExcecutaTarefa (self):
        print("%s executa a tarefa" %self.nome)

    def Pertence (self):
        print ("%s pertence ao projeto" %self.nome)






