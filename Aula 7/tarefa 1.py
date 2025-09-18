from flask import Flask, request

app = Flask(__name__)
nome = ''
senha = ''
@app.route('/ver' , methods=['GET'])
def getRoute():
    global nome
    if not nome:
        return 'Usuário não cadastrado'
    return f'Usuário: {nome}\n Senha: {senha}'

@app.route('/cadastrar' , methods=['POST'])
def createAccount():
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    create_account(nome, senha)   
    return f'Usuário {nome} cadastrado com sucesso!'

@app.route('/atualizarCadastro' , methods=['POST'])
def update_account():
    nomeForm = request.form.get('nome')
    change_name(nomeForm)
    return f'Cadastro atualizado para: {nome}'

@app.route('/atualizarSenha' , methods=['POST'])
def update_password():
    senhaForm = request.form.get('senha')
    change_password(senhaForm)   
    return f'senha atualizada com sucesso!'

def create_account(novo_nome, nova_senha):
    global nome, senha
    nome = novo_nome
    senha = nova_senha
    return

def change_name(novo_nome):
    global nome
    nome = novo_nome
    return

def change_password(nova_senha):
    global senha
    senha = nova_senha
    return
    
if __name__ == '__main__':
    app.run(debug=True)