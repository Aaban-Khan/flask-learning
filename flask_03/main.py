from flask import Flask, render_template, request, redirect, flash, url_for, session
import os
import google.generativeai as genai
from datetime import datetime

app = Flask(__name__)
app.secret_key = "wassup"

API_KEY = "AIzaSyDFrCtfM77rAz-LgUbaCxBaSlPA7tRbsu0"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")
chat_bot = model.start_chat()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["GET", "POST"])
def chat():
    if "user" not in session:
        return redirect(url_for("login"))

    prompt = ""
    response = ""
    if request.method == "POST":
        prompt = request.form.get("prompt")
        if prompt:
            try:
                result = chat_bot.send_message(prompt)
                response = result.text
            except Exception as e:
                print(f"Error as, {e}")
    return render_template("chat.html", response=response, prompt=prompt)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email == "aaban@gmail.com" and password == "1234":
            session["user"] = email
            return redirect(url_for("chat"))
        else:
            flash("WRONG Email/Password, try again!", "error")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
