from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    hobbies_list = ["Coding", "Reading", "Hiking"]
    return render_template("index.html", user_name="Sam" , hobbies = hobbies_list)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)