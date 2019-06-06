from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "Secret"

@app.route("/")
def index():
    if "message" not in session:
        session["message"] = ""
        session["color"] = "white"
    if "randomNum" not in session:
        session["randomNum"] = round(random.random()*99 + 1)
    print(session["randomNum"])
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    guessNum = int(request.form["num"])
    if guessNum == session["randomNum"]:
        session["message"] = "Your guess is correct!"
        session["color"] = "green"
    elif guessNum > session["randomNum"]:
        session["message"] = "Too High"
        session["color"] = "red"
    elif guessNum < session["randomNum"]:
        session["message"] = "Too Low"
        session["color"] = "red"
    return redirect("/")

@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)