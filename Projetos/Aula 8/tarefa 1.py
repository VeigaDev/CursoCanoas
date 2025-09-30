from flask import Flask, request

app = Flask(__name__)

usuarios = {}

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    global usuarios
    return usuarios if usuarios else 'Nenhum usuário cadastrado.'

@app.route('/usuario/<int:id>', methods=['GET'])
def get_usuario(id):
    global usuarios
    for usuario in usuarios:
        if usuario == id:
            return usuarios[usuario]
    return f'Usuário com id {id} não encontrado!'

@app.route('/usuario/<int:id>', methods=['DELETE'])
def remover_usuario(id):
    global usuarios
    for usuario in usuarios:
        if usuario == id:
            del usuarios[usuario]
            return f'Usuário com id {id} removido com sucesso!'
    return f'Usuário com id {id} não encontrado!'

@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    global usuarios
    usuario = {
        "nome": request.form.get('nome'),
        "email": request.form.get('email'),
        "idade": request.form.get('idade')
    }
    usuarios.update({len(usuarios)+1: usuario})
    return f"Usuário {usuario["nome"]} cadastrado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True) 