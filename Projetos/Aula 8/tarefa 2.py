from flask import Flask, request
app = Flask(__name__)

produtos = {}

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    global produtos
    if not produtos:
        return 'Ainda não há produtos cadastrados'
    else: 
        return produtos
    
@app.route('/produto/<int:id>', methods=['GET'])
def obter_produto(id):
    global produtos
    for produto in produtos:
        if produto == id:
            return produtos[produto]
    return f'Produto com id {id} não encontrado!'

@app.route('/adicionarProduto', methods=['POST'])
def adicionar_produto():
    global produtos
    nome = request.form.get('nome')
    preco = request.form.get('preco')
    estoque = request.form.get('estoque')
    
    if not nome or not preco:
        return 'Nome e preço são obrigatórios!'
    
    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque if estoque else 0
    }

    produtos[produto["id"]] = produto   
    
    return f'Produto {nome} adicionado com sucesso!'

@app.route('/atualizarProduto/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    global produtos
    nome = request.form.get('nome')
    preco = request.form.get('preco')
    estoque = request.form.get('estoque')
    
    for produto in produtos:
        if produto == id:
            produtoAtualizado = produtos[produto]
            produtoAtualizado["nome"] = nome if nome else produtoAtualizado['nome']
            produtoAtualizado['preco'] = preco if preco else produtoAtualizado['preco']
            produtoAtualizado['estoque'] = estoque if estoque else produtoAtualizado['estoque']
            return f'Produto com id {id} atualizado com sucesso!\n {produtoAtualizado}'
    
    return f'Produto com id {id} não encontrado!'

@app.route('/removerProduto/<int:id>', methods=['DELETE'])
def remover_produto(id):
    global produtos
    for produto in produtos:
        if produto == id:
            produtos.pop(produto)
        return f'Produto com id {id} removido com sucesso!'
    return f'Produto com id {id} não encontrado!'

if __name__ == '__main__':
    app.run(debug=True)