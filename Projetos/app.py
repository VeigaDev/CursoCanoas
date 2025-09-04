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
    return "About Page" 

if __name__ == '__main__':
    app.run(debug=True) 