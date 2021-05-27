from flask import Flask, render_template
import socket, subprocess

app = Flask(__name__)
mensaje=[]


@app.route("/")
def index():
    return render_template('index.html',mensaje=['System Check',''])

@app.route("/<parametro>")
def mostrar(parametro):
    if parametro=="ip":
        return render_template('index.html', mensaje=['IP', socket.gethostbyname(socket.gethostname())])
    elif parametro=="nombre":
        return render_template('index.html', mensaje=['NOMBRE', socket.gethostname()])
    elif parametro=="reinicia":
        return render_template('index.html', mensaje=['reinicia', subprocess.call(["shutdown", "/r", "-t", "60"])])
    else:
        return render_template('index.html',mensaje=['Error','Parámetro no válido, haz clic en el menú superior'])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
