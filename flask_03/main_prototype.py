from flask import Flask, render_template, request, redirect, flash, url_for, session
import os
import google.generativeai as genai
from datetime import datetime

app = Flask(__name__)
app.secret_key = "wassup"

tasks = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/getStarted", methods=["GET", "POST"])
def getStarted():
    if "user" not in session:
        flash("Pahle Login kar bhai, Error")
        return redirect(url_for("login"))

    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
            return redirect(url_for("getStarted"))
    return render_template("getStarted.html", tasks=tasks)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email == "aaban@gmail.com" and password == "1234":
            session["user"] = email
            return redirect(url_for("getStarted"))
        else:
            flash("Bhai galat email ya password hai!", "error")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)

import google.generativeai as genai
import textwrap
from colorama import Fore, Style
import pyttsx3

engine = pyttsx3.init()
from datetime import datetime
import os

API_KEY = "AIzaSyDFrCtfM77rAz-LgUbaCxBaSlPA7tRbsu0"


def init_model():

    if not API_KEY:
        raise ValueError("API key is missing!")

    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash")

    return model.start_chat()


def ask_gemini(chat, user_input):
    try:
        response = chat.send_message(user_input)
        return response.text

    except Exception as e:
        return f"Error as {e}"


def save_data(response, user_input, prompt_num):

    if not [response, user_input, prompt_num]:
        return

    chat_date = f"database/data_{datetime.now().strftime("%d-%b-%Y")}.txt"
    chat_time = datetime.now().strftime("%I:%M:%S %p")

    if not os.path.exists("database"):
        os.makedirs("database")

    if prompt_num <= 1:
        with open(chat_date, "a") as file:
            file.write(f"Saving Data...\n\n")

    with open(chat_date, "a") as file:
        file.write(f"At {chat_time}\nPrompt: {user_input} \nBot: {response}\n\n")


def main():
    print(f"{Fore.LIGHTMAGENTA_EX}\nHello from gen-ai! Aaban{Style.RESET_ALL}")
    chat = init_model()
    use_voices = True
    prompt_num = 0

    while True:
        user_input = (
            input(Fore.LIGHTCYAN_EX + "\nYou> " + Style.RESET_ALL).lower().strip()
        )

        if user_input in ["mute", "voice off"]:
            use_voices = False
            print(f"{Fore.YELLOW} Voice turned Off {Style.RESET_ALL}")
            continue
        elif user_input in ["unmute", "un-mute", "voice on"]:
            use_voices = True
            print(f"{Fore.GREEN} Voice turned ON {Style.RESET_ALL}")
            continue

        if user_input in ["exit", "quit", "q", "n"]:
            print(f"{Fore.RED}Exiting...Take care {Style.RESET_ALL}")
            break
        elif user_input == "":
            continue
        else:

            if user_input not in ["unmute", "un-mute", "voice on", "mute", "voice off"]:
                response = ask_gemini(chat, user_input)
                prompt_num += 1
                save_data(response, user_input, prompt_num)

            if use_voices:
                engine.say(str(response))
                engine.runAndWait()
            print(
                Fore.BLUE
                + "\nGemini> "
                + textwrap.fill(response, width=100)
                + Style.RESET_ALL
            )


if __name__ == "__main__":
    main()


# def login():
#     users = 0

#     if request.method == "POST":
#         email = request.form["email"]
#         password = request.form["password"]
#         if email and password:
#             users += 1
#             save_data(email,password,users)
#             return redirect(url_for("getStarted"))
#         else:
#             flash("Something Went WRONG!!", "error")
#             return redirect(url_for("login"))

#     return render_template("login.html")


# def save_data(email,password,users):

#     if not os.path.exists('database'):
#         os.makedirs('database')

#     with open("database/login.txt", "a", encoding="utf-8") as file:
#         file.write(f"{users}) Email: {email}\nPassword: {password}\n\n")
