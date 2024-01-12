from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Oregunwa_19@localhost/students'
db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(40))
    fname = db.Column(db.String(40))
    pet = db.Column(db.String(40))
# Students table definition

    def __init__(self, fname, lname, pet):
        self.fname = fname
        self.lname = lname
        self.pet = pet
    # constructor


@app.route("/")
def index():
    return render_template("index.html")
# Route for index page


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        pet = request.form['pets']
# Decorator that maps the /submit URL to the submit() function and allows both GET and POST requests

        # Create a new Student object with the first name, last name, and pet name obtained from the form data
        student = Student(fname, lname, pet)
        # Add the newly created Student object to the session
        db.session.add(student)
        # Commit the session to save the changes to the database
        db.session.commit()

        studentResult = db.session.query(Student).filter(Student.id == 1)
        for result in studentResult:
            print(result.fname)

        return render_template('success.html', data=fname)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
