from flask import Flask #Importa função flask da biblioteca flask

app = Flask(__name__) #Atribui a aplicação para a variável app

@app.route('/inicio') #Cria nova rota
def ola():
    return '<h1>Olá Mundo!</h1>'

app.run()