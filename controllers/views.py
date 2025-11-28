from flask import render_template, redirect, request, url_for
from app import app, db
from app.models.recado import Recado

@app.route("/")
def index():
    busca = request.args.get("busca", "")

    if busca:
        recados = Recado.query.filter(Recado.titulo.contains(busca)).all()
    else:
        recados = Recado.query.all()

    return render_template("index.html", recados=recados, busca=busca)


@app.route("/adicionar", methods=['GET','POST'])
def adicionar():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        mensagem = request.form.get("mensagem")

        if titulo and mensagem:
            novo = Recado(titulo=titulo, mensagem=mensagem)
            db.session.add(novo)
            db.session.commit()

        return redirect(url_for('index'))

    return render_template("adicionar.html")


@app.route("/excluir/<int:id>")
def excluir(id):
    recado = Recado.query.get(id)
    db.session.delete(recado)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/editar/<int:id>", methods=["POST"])
def editar(id):
    recado = Recado.query.get(id)
    recado.titulo = request.form.get("novo_titulo")
    recado.mensagem = request.form.get("nova_msg")
    db.session.commit()

    return redirect(url_for("index"))