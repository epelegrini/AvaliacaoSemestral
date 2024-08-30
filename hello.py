from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)
alunos = []

@app.route('/')
def index():
    page = request.args.get('page')
    if page == 'nao-disponivel':
        return render_template('nao_disponivel.html')
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/cadastrar-aluno', methods=['GET', 'POST'])
def cadastrar_aluno():
    if request.method == 'POST':
        nome = request.form['nome']
        disciplina = request.form['disciplina']
        alunos.append({'nome': nome, 'disciplina': disciplina})
        return redirect(url_for('cadastrar_aluno'))
    return render_template('cadastro_alunos.html', alunos=alunos)

@app.route('/listar-alunos')
def listar_alunos():
    return render_template('listar_alunos.html', alunos=alunos)

if __name__ == '__main__':
    app.run(debug=True)
