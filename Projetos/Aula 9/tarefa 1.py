from flask import Flask, request

app = Flask(__name__)  

senhas = {
    "senha123": True,
    "python123" : True,
    "Flask2025": True,
}

@app.route('/verificarSenha/<string:senha>', methods=['GET'])
def verificar_senha(senha):
    if senha in senhas:
        return f'Senha "{senha}" é válida.'
    else:
        return f'Senha "{senha}" é inválida.'
if __name__ == '__main__':
    app.run(debug=True)