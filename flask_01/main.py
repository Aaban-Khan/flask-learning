'''# ================================
# 🧠 01 — Basic Flask Setup + Routing
# ================================

# Flask import kar rahe hain — ye main library hai jo web app create karti hai
from flask import Flask

# Flask app ko initialize kar rahe hain (jaise ek engine ready karna)
app = Flask(__name__)  # __name__ ka matlab hai current file ko Flask identify karega

# =====================
# 👇 Route define kar rahe hain
# =====================

# Ye '/' route hai, jo homepage ko represent karta hai
# Jaise tu browser me localhost:5000 likhega, to yeh function chalega
@app.route('/')
def home():
    return "Hello world"  # Browser me yeh text dikhai dega

# Dusra route '/about' ke liye hai
# Jab tu browser me localhost:5000/about likhega, to yeh chalega
@app.route('/about')
def about():
    return "This is an About page"

# =====================
# 🚀 Flask app ko run karna
# =====================

# __name__ == "__main__" ka matlab yeh file directly run ho rahi hai (import nahi)
if __name__ == "__main__":
    app.run(debug=True)  # debug=True se app auto-reload hota hai jab tu file save kare




# ================================
# 🧠 02 — HTML Templating with Flask
# ================================

# Flask + render_template import kiya
# render_template HTML files ko backend se serve karne ke kaam aata hai
from flask import Flask, render_template

# Flask app initialize kiya
app = Flask(__name__)

# =====================
# 👇 Home route - HTML page render karna
# =====================

# Jab koi user '/' par aaye, to index.html file browser me bhejna
# index.html templates folder ke andar hona chahiye (Flask default structure)
@app.route('/')
def home():
    return render_template('index.html')  # HTML file render kar raha hai

# =====================
# 👇 About route - HTML + Python data send
# =====================

# Ab yahan HTML me Python ka data bhi bhej rahe hain (name = "aaban")
# Ye data HTML me {{ name }} likhne par visible hoga (Jinja2 template syntax)
@app.route('/about')
def about():
    return render_template('about.html', name="aaban")

# =====================
# 🚀 Flask app ko run karna (debug mode on)
# =====================
if __name__ == "__main__":
    app.run(debug=True)'''


from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name = "Aaban")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/base')
def base():
    return render_template('utilities/base.html')

# form ka route, GET se data url me dikhta hai, Post se hidden rehta hai!! isse methods naam ke arrray me dikhana jarui hota hia!
@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':    # agar Post method h
        name = request.form['username']     #form se name me se username nikala, aise ho agar password hua to password likh kar nikal sakte hai!
        return render_template('utilities/base.html', name=name)       #login ke baad new page render karaya
    return render_template('submit.html')           # ⚠️ Agar GET method hai (user ne bas page khola hai, form fill nahi kiya) to form dikhana hai

if __name__ == "__main__":
    app.run(debug=True)


