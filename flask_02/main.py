from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


"""🔍 Breakdown Explanation:
Concept	Bro Style Breakdown
GET by default hota hai	✅
Bilkul sahi! Agar tu <form> me method="POST" nahi likhega, toh GET method by default use hota hai.
GET Form dikhata hai
Sahi point. Jab user pehli baar route pe aata hai (/submit), to GET method se page load hota hai — yani ki form dikhaya jaata hai.
POST form ke fill hone ke baad hota hai	✅
Ye bhi sahi hai. Jab user form submit karta hai (button dabata hai), toh POST method activate hota hai, jo backend ko data bhejta hai aur processing start karta hai."""


# "By default, a form uses GET method, which is used to display the form. Once the user fills the form and submits, the POST method is triggered to send data to the backend for processing."
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]
        if name and password != "":
            return f"Welcome {name}! Your Password is {password}"
        else:
            return f"SOmething went wrong"
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
