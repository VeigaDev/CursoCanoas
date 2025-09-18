from flask import Flask, request

app = Flask(__name__)

@app.route('/findword', methods=['POST'])
def find_word():
    frase = request.form.get('frase')
    keyword = request.form.get('palavra-chave')
    if not frase:
        return "Nenhuma frase fornecida!"
    find = frase.find(keyword)
    if find == -1:
        return f'Palavra {keyword} não encontrada!'
    else:
        return f'Palavra {keyword} encontrada na posição {find}!'

if __name__ == '__main__':
    app.run(debug=True)
    