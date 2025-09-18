from flask import Flask, request

app = Flask(__name__)
@app.route('/tarefa10' , methods=['POST'])
def phraseRoute():
    phrase = request.form.get('frase')
    if not phrase:
        return "Nenhuma frase fornecida!"
    
    count_characters = len(phrase)
    count_vowels = phrase.lower().count('e')
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    replace_vowels = ''
    phrase_replaced = phrase
    
    for v in vowels:
        replace_vowels = phrase_replaced.replace(v, '*')
        phrase_replaced = replace_vowels
    return f'Frase em maiúsculas: {phrase.upper()}\nQuantas vezes aparece a letra "e": {count_vowels}\nFrase com as vogais substituidas: {phrase_replaced}\nNúmero de caracteres: {count_characters}'

if __name__ == '__main__':
    app.run(debug=True)
    