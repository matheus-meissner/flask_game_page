from flask import Flask, render_template #Importa função flask da biblioteca flask

app = Flask(__name__) #Atribui a aplicação para a variável app

@app.route('/inicio') #Cria nova rota
def ola():
    return render_template('lista.html') #Importa HTML

app.run()