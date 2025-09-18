from flask import Flask, request

app = Flask(__name__)
@app.route('/ping')
def archive_validate(): 
    archive_name = request.form.get('arquivo')
    if not archive_name:
        return "Nenhum nome de arquivo informado!"
    if archive_name.lower().endswith('.pdf') and archive_name.lower().startswith('.relatorio'):
        return "Arquivo válido!"
    else:
        return "Arquivo inválido! Apenas relatorio.pdf é permitido."
if __name__ == '__main__':
    app.run(debug=True)
    