from flask import Flask, request

app = Flask(__name__)
@app.route('/email', methods=['POST'])
def emailRoute():
    email = request.form.get('email')
    if not email:     
        return "Nenhum email fornecido!"
    if validate_email(email.lower()):
        return "Email válido!"
    else:   
        return "Email inválido!" 
    
def validate_email(email):
    if "@" in email and "." in email.split("@")[-1]:
        return True
    return False

if __name__ == '__main__':
    app.run(debug=True)
    