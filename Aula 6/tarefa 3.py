from flask import Flask, request

app = Flask(__name__)

@app.route('/badwords' , methods=['POST'])

def filter_bad_words():
    text = request.form.get('texto')
    censored_text = profanity_filter(text)
    return f'Texto censurado: {censored_text}'

def profanity_filter(text):
    return text.replace('chato', '*****')

if __name__ == '__main__':
    app.run(debug=True) 