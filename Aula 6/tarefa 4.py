from flask import Flask, request

app = Flask(__name__)

@app.route('/vowels' , methods=['POST'])

def vowels():
    text = request.form.get('texto')
    count_vowels = text.count('a')
    return f'Número de vogais "a": {count_vowels}'

if __name__ == '__main__':
    app.run(debug=True)