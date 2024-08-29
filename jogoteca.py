from flask import Flask, render_template #Importa função flask da biblioteca flask

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

app = Flask(__name__) #Atribui a aplicação para a variável app

@app.route('/inicio') #Cria nova rota
def ola():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
    jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista) #Importa HTML, define variável

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

app.run()