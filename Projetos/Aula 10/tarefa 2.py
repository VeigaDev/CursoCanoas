from flask import Flask, request, jsonify

app = Flask(__name__)

cursos = {
    101: {'professor': 'Alice', 'curso': 'Backend Python'},
    102: {'professor': 'Bob', 'curso': 'Frontend React'},
    103: {'professor': 'Charlie', 'curso': 'Data Science'},
}

@app.route('/')
def home():
    global cursos
    return cursos

@app.route('/curso', methods=['POST'])
def adicionar_curso():
    global cursos
    nome = request.form.get('professor')
    curso = request.form.get('curso')
    resposta = verifica_dados(nome, curso)

    if resposta:
        return resposta
    else:
        ids = cursos.keys()
        proximoId= max(ids) + 1
        curso = { 
            proximoId : {
                "professor": nome,
                "curso": curso
            }
        }
        cursos.update(curso)
        return f"curso {curso} cadastrado com sucesso!"

@app.route('/verCurso/<int:id>')
def ver_cadastro(id):
    global cursos
    if id in cursos:
        return jsonify(cursos[id])
    else: 
        return "Não existe esse curso cadastrado"
    
@app.route('/alterarCadastro/<int:id>', methods=["POST"])
def alterar_cadastro(id):
    global cursos
    if id in cursos:
        
        curso = cursos[id]
        verifica_dados(request.form.get('professor'), request.form.get('curso'))
        curso["curso"] = request.form.get('curso')
        curso["professor"] = request.form.get('professor')
        return f"Dados atualizados com sucesso!\n {jsonify(curso)}"
    else: 
        return "curso não encontrado" 
    
@app.route('/deletarCadastro/<int:id>', methods=['DELETE'])
def deletar_cadastro(id):
    global cursos
    if id in cursos:
        cursos.pop(id)
        return f"Cadastro excluído com sucesso\n {jsonify(cursos)}"
    else: return "Cadastro não encontrado"

def verifica_dados(nome, curso):
    if nome == '':
        return "O campo PROFESSOR está em branco"
    elif curso == '':
        return "O campo CURSO está em branco"
    else: return


if __name__ == '__main__':
    app.run(debug=True)