from flask import Flask, render_template

app = Flask(__name__, template_folder="templates/")

@app.route('/')
@app.route('/home')
@app.route('/home/')
@app.route('/templates/home.html')
def home():
    return render_template("home.html")

@app.route('/events')
@app.route('/events/')
@app.route('/templates/events.html')
def events():
    return render_template("events.html")

@app.route('/schedules')
@app.route('/schedules/')
@app.route('/templates/schedules.html')
def schedules():
    return render_template("schedules.html")

@app.route('/about_us')
@app.route('/about_us/')
@app.route('/templates/about_us.html')
def about_us():
    return render_template("about_us.html")

@app.route('/our_team')
@app.route('/our_team/')
@app.route('/templates/our_team.html')
def our_team():
    return render_template("our_team.html")

# if __name__ == "__main__":
#     app.run(port=5505)