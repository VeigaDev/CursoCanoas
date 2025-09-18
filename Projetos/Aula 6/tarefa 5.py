from flask import Flask, request

app = Flask(__name__)
@app.route('/password', methods=['POST'])

def password_strength():
    password = request.form.get('senha')
    if password is None:
        return 'Senha não fornecida', 400
    if len(password) < 6 or len(password) > 10:
        return 'Senha deve conter entre 6 e 10 caracteres'
    else: 
        return 'Senha válida' 

if __name__ == '__main__':
    app.run(debug=True)
    