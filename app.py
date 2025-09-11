from flask import Flask, request
import sys
sys.path.append(r'c:\Users\03573005055\Documents\Projetos\Aula 5')
from file import ping
app = Flask(__name__)

@app.route('/ping')
def ping_route():
    return ping()

@app.route('/formulario' , methods=['POST'])
def formulario():
    nome = request.form.get('nome')
    idade = request.form.get('idade')
    endereco = request.form.get('endereco')
    return f"Nome: {nome}, Idade: {idade}, Endereço: {endereco}"

@app.route('/rpg/<nivel>')
def rpg(nivel):
    nivel = int(nivel)
    if nivel < 100:
        return "Novato"
    elif nivel < 500:
        return "Intermediário"
    else:
        return "Avançado"
    
@app.route('/cupom/<valor>/<cupom>')
def cupom(valor, cupom):
    cupom = cupom.lower()
    valor = float(valor)
    if cupom == "desconto10":
        valor_cupom = 10
        valor = valor - (valor * valor_cupom / 100)
        return f"Valor com desconto: R$ {valor:.2f}"
    elif cupom == "desconto20":
        valor_cupom = 20
        valor = valor - (valor * valor_cupom / 100)
        return f"Valor com desconto: R$ {valor:.2f}"
    else:
        return "Cupom inválido!"   
       
if __name__ == '__main__':
    app.run(debug=True) 