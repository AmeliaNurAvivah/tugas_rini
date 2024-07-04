from flask import Flask, render_template, redirect, url_for, request 

app = Flask (__name__)

@app.route("/")
def menu():
  return render_template("menu.html")

@app.route ("/masuk", methods=["POST", "GET"])
def masuk():
    if request.method =="GET" :
        return render_template("masuk.html")

    if request.method =="POST" : 
        username = "Rini"
        password = "060603"

        input_username = request.form.get("username")
        input_password = request.form.get("password")

        if input_username == username and input_password == password:
            return redirect(url_for("Home"))
        else :
            return redirect(url_for("masuk"))
        
@app.route("/Home")
def Home():
    return render_template("Home.html")

@app.route("/transfer")
def transfer():
    return render_template("transfer.html")

@app.route("/tarik_tunai")
def tarik_tunai():
    return render_template("tarik_tunai.html")

@app.route("/isi_saldo")
def isi_saldo():
    return render_template("isi_saldo.html")

if __name__ == '__main__':
    app.run(debug=True)
