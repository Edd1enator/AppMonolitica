from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    numero1 = request.form["numero1"]
    numero2 = request.form["numero2"]
    operacion = request.form["operacion"]

    resultado = 0

    if operacion == "suma":
        resultado = int(numero1) + int(numero2)
    elif operacion == "resta":
        resultado = int(numero1) - int(numero2)
    elif operacion == "multiplicacion":
        resultado = int(numero1) * int(numero2)
    elif operacion == "division":
        resultado = int(numero1) / int(numero2)

    return render_template("resultado.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
