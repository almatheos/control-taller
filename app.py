from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "clave_secreta_para_sesiones"  # cámbiala por una tuya

# Simulación de usuarios (más adelante lo harás con SQL)
USUARIOS = {"admin": "1234", "mecanico": "abcd"}

@app.route("/")
def home():
    if "usuario" in session:
        return render_template("home.html", usuario=session["usuario"])
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        clave = request.form["clave"]
        if usuario in USUARIOS and USUARIOS[usuario] == clave:
            session["usuario"] = usuario
            return redirect(url_for("home"))
        else:
            return "Usuario o contraseña incorrectos"
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
