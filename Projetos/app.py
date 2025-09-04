from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/rpg/<nivel>')
def about(nivel):
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