from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/attendance')
def attendance():
    return render_template('attendance.html')

@app.route('/studentmgt')
def studentmgt():
    return render_template('studentmgt.html')

if __name__ == "__main__":
    app.run(debug=True)
