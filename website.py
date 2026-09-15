from flask import Flask, render_template

website = Flask(__name__)

@website.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    website.run(host="0.0.0.0", port=5000, debug=False)