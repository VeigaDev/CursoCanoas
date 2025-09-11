from flask import Flask, request
import re

app = Flask(__name__)
@app.route('/formulario' , methods=['POST'])

def forms():
    name = request.form.get('nome')
    if not name or len(name) < 2:
        return "Nome inválido! Deve ter pelo menos 3 caracteres."
    
    email = request.form.get('email')
    if not validate_email(email):
        return "Email inválido!"
    
    password = request.form.get('senha')
    if not validate_password(password):
        return "Senha inválida! Deve ter pelo menos 8 caracteres e um caractere especial."

    date_birth = request.form.get('dia_nascimento')
    month_birth = request.form.get('mes_nascimento')
    year_birth = request.form.get('ano_nascimento')
    if not date_birth or not month_birth or not year_birth:
        return "Data de nascimento incompleta!"
    try:
        date_birth = int(date_birth)
        month_birth = int(month_birth)
        year_birth = int(year_birth)
        if date_birth < 1 or date_birth > 31 or month_birth < 1 or month_birth > 12 or year_birth < 1900 or year_birth > 2024:
            return "Data de nascimento inválida!"
    except ValueError:
        return "Data de nascimento inválida!"   
    return f"Nome: {name}, Email: {email}, Senha: {'*' * len(password)}, Data de Nascimento: {date_birth}/{month_birth}/{year_birth}"

def validate_password(password):
    pattern = r'^(?=.*[\W_]).{8,}$'
    return re.match(pattern, password) is not None

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None
    
if __name__ == '__main__':
    app.run(debug=True) 
    