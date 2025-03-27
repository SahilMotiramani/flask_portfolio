from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Load projects from JSON
def load_projects():
    with open("projects.json", "r") as file:
        return json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    projects = load_projects()
    return render_template("portfolio.html", projects=projects)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        if not name or not email or not subject or not message:
            return "All fields are required!", 400

        return redirect(url_for("success", name=name, email=email, subject=subject, message=message))

    return render_template("contact.html")

@app.route("/success")
def success():
    name = request.args.get("name")
    email = request.args.get("email")
    subject = request.args.get("subject")
    message = request.args.get("message")
    return render_template("success.html", name=name, email=email, subject=subject, message=message)

if __name__ == "__main__":
    app.run(debug=True)
