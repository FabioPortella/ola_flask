from models import Pessoas, Usuarios

def inserir():
    pessoa = Pessoas(nome='Rafael', idade=26)
    print(pessoa)
    pessoa.save()


def consultar():
    pessoa = Pessoas.query.all()
    for pess in pessoa:
        print(f'{pess.id} - {pess.nome} - {pess.idade}')


def alterar():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.nome = "Adriana"
    pessoa.save()


def excluir():
    pessoa = Pessoas.query.filter_by(nome='Helena').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print (usuarios)

if __name__=='__main__':
    insere_usuario('Juliana', '1234')
    insere_usuario('Fabio', '1234')
    consulta_todos_usuarios()
    #insere_pessoas()
    #alterar()
    #excluir()
    #consultar()