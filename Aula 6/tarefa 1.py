from flask import Flask, request

app = Flask(__name__)
@app.route('/nome' , methods=['POST'])
def form_name():
    name = request.form.get('nome')
    if not name or len(name) < 3:
        return "Nome inválido! Deve ter pelo menos 3 caracteres."
    return f'Nome com a Primeira Letra Maiúscula: {name.capitalize()}\nNome Maiúsculo: {name.upper()}\nNome Minisculo: {name.lower()}'

if __name__ == '__main__':
    app.run(debug=True) 