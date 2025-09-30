from flask import Flask, request
app = Flask(__name__)

cupons = {
    "CUPOM10": 10,
    "CUPOM20": 20,
}

@app.route('/finalizarCompra/<float:valor>/<string:cupom>/', methods=['GET'])

def verificar_cupom(valor, cupom):
    cupom = cupom.upper()
    if cupom in cupons:
        desconto = cupons[cupom] or 0
        valor_final = valor - (valor * desconto / 100)
        return f'Cupom "{cupom}" aplicado! Valor original: R${valor:.2f}. Valor com desconto: R${valor_final:.2f}.'
    else:
        return f'Cupom "{cupom}" é inválido. Valor total: R${valor:.2f}.'
    
if __name__ == '__main__':
    app.run(debug=True)