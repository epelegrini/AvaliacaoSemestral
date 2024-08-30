from datetime import datetime
from flask import Flask, render_template, request, make_response, redirect, abort, urlfor
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)
alunos = []


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
     return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/aluno/<nome>/<prontuario>/<inst>')
def aluno(nome, prontuario, inst):
    return render_template('identificacao.html', nome=nome, prontuario=prontuario, inst=inst)

@app.route('/contextorequisicao/<nome>')
def contextorequisicao(nome):
    user_agent = request.headers.get('User-Agent');
    agent      = "{}".format(user_agent);
    ip         = "{}".format(request.remote_addr);
    host       = "{}".format(request.host);
    return render_template('contextorequisicao.html', nome=nome, agent=agent, ip=ip, host=host)

@app.route('/cadastrar-aluno', methods=['GET', 'POST'])
def cadastrar_aluno():
    if request.method == 'POST':
        nome = request.form['nome']
        disciplina = request.form['disciplina']
        alunos.append({'nome': nome, 'disciplina': disciplina})
        return redirect(url_for('listar_alunos'))
    return render_template('cadastro_alunos.html')



@app.route('/listar-alunos')
def listar_alunos():
    return render_template('listar_alunos.html', alunos=alunos)

if __name__ == '__main__':
    app.run(debug=True)
