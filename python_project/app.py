from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    #dados que serão calculados em Python
    titulo_pagina = "Dashboard de Demonstração"
    aluno = {"nome": "Lucas", "curso": "Analista de Sistemas", "nota": 9.5}
    status = "Aprovado" if aluno["nota"] >= 5 else "Reprovado"

    #Essa parte envia as imnformações para o template HTML
    return render_template(
    "index.html",
    titulo=titulo_pagina,
    usuario=aluno,
    resultado=status
    )

if __name__ == "__main__":
    app.run(debug=True)



     