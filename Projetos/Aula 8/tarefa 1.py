from flask import Flask, request

app = Flask(__name__)

usuario = {
    "nome": "William",
    "idade": 30,
    "email": "william.veiga@live.com",
    "cidade": "Novo Hamburgo"
}


@app.route('/perfil', methods=['GET'])
def get_usuario():
    return f"Nome: {usuario.get('nome')}, Idade: {usuario.get('idade')}, Email: {usuario.get('email')}, Cidade: {usuario.get('cidade')}"

if __name__ == '__main__':
    app.run(debug=True) 