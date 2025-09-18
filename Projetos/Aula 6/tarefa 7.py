from flask import Flask, request

app = Flask(__name__)
@app.route('/nickname', methods=['POST'])
def nicknameFunction():
    fullname = request.form.get('nome')
    if not fullname:
        return "Nenhum nome fornecido!"
    names = fullname.split(' ')
    nickname = '-'.join(names)
    return f'Seu apelido é: {nickname}'
        
if __name__ == '__main__':
    app.run(debug=True)
    
 