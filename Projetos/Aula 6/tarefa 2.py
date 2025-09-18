from flask import Flask, request

app = Flask(__name__)
@app.route('/limpadorDeFrase' , methods=['POST'])
def clean_sentence():
    sentence = request.form.get('frase')
    if not sentence:
        return "Frase inválida! Não pode estar vazia."
    else:
        cleaned_sentence = sentence.strip().replace("  ", " ")  
        return f'Frase limpa: {cleaned_sentence}'
       
if __name__ == '__main__':
    app.run(debug=True)