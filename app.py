from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///responses.db'  # SQLite database for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the database model
class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    question1 = db.Column(db.String(200), nullable=False)
    question2 = db.Column(db.String(200), nullable=False)
    question3 = db.Column(db.String(200), nullable=False)
    question4 = db.Column(db.String(200), nullable=False)
    question5 = db.Column(db.String(200), nullable=False)

    def __init__(self, email, question1, question2, question3, question4, question5):
        self.email = email
        self.question1 = question1
        self.question2 = question2
        self.question3 = question3
        self.question4 = question4
        self.question5 = question5

# Create the database tables
with app.app_context():
    db.create_all()

def email_exists(email):
    response = Response.query.filter_by(email=email).first()
    return response is not None

def save_response(data):
    new_response = Response(
        email=data["email"],
        question1=data["question1"],
        question2=data["question2"],
        question3=data["question3"],
        question4=data["question4"],
        question5=data["question5"]
    )
    db.session.add(new_response)
    db.session.commit()

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        email = request.form.get("email")
        if email_exists(email):
            flash("This email has already been used to submit a response.")
            return redirect(url_for("form"))
        
        responses = {
            "email": email,
            "question1": request.form.get("question1"),
            "question2": request.form.get("question2"),
            "question3": request.form.get("question3"),
            "question4": request.form.get("question4"),
            "question5": request.form.get("question5"),
        }
        save_response(responses)
        return redirect(url_for("thank_you"))

    return render_template("forms.html")

@app.route("/thank-you")
def thank_you():
    return render_template("thankyou.html")

@app.route("/view-responses")
def view_responses():
    responses = Response.query.all()
    for response in responses:
        print(response.email, response.question1, response.question2, response.question3, response.question4, response.question5)
    return "1234"


if __name__ == "__main__":
    app.run(debug=True)
