from flask import Flask, request, jsonify

app = Flask(__name__)

alunos = {
    101: {'nome': 'Alice', 'nota': 9.0, 'curso': 'Backend Python'},
    102: {'nome': 'Bob', 'nota': 8.5, 'curso': 'Frontend React'},
    103: {'nome': 'Charlie', 'nota': 2.3, 'curso': 'Data Science'},
}

@app.route('/aluno', methods=['POST'])
def adicionar_aluno():
    global alunos
    
    nome = request.form.get('nome')
    nota = request.form.get('nota')
    curso = request.form.get('curso')
    resposta = verifica_dados(nome, float(nota), curso)

    if resposta:
        return resposta
    else:
        ids = alunos.keys()
        proximoId= max(ids) + 1
        aluno = { 
            proximoId : {
                "nome": nome,
                "nota": float(nota),
                "curso": curso
            }
        }
        alunos.update(aluno)
        return f"Aluno {nome} cadastrado com sucesso!"

@app.route('/verCadastro/<int:id>')
def ver_cadastro(id):
    global alunos
    if id in alunos:
        return jsonify(alunos[id])
    else: 
        return "Não existe esse cadastro"
    
@app.route('/alterarCadastro/<int:id>', methods=["POST"])
def alterar_cadastro(id):
    global alunos
    if id in alunos:
        nota = request.form.get('nota')
        verifica_dados('nome', float(nota), 'curso')
        aluno = alunos[id]
        aluno["nota"] = float(nota)
        return f"Nota atualizada com sucesso!\n {jsonify(aluno)}"
    else: 
        return "Aluno não encontrado" 
    
@app.route('/deletarCadastro/<int:id>', methods=['DELETE'])
def deletar_cadastro(id):
    global alunos
    if id in alunos:
        alunos.pop(id)
        return f"Cadastro excluído com sucesso\n {jsonify(alunos)}"
    else: return "Cadastro Não encontrado"

def verifica_dados(nome, nota, curso):
    if nome == '':
        return "O campo NOME está em branco"
    elif nota == '':
        return "O campo NOTA está em branco"
    elif not isinstance(nota, float):
        return "O campo NOTA recebe apenas números"
    elif curso == '':
        return "O campo CURSO está em branco"
    else: return


if __name__ == '__main__':
    app.run(debug=True)