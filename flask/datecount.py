from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import datetime as dt

def calc_next_birthday(dob):
    today = dt.date.today()

    line1=f"My date of birth is: {dob}"
    line2=f"Today is: {today}"
    birthday_this_year = dt.date(today.year, dob.month, dob.day)
    birthday_next_year = dt.date(today.year+1, dob.month, dob.day)

    if birthday_this_year > today:
        next_birthday = birthday_this_year
    else:
        next_birthday = birthday_next_year

    line3=f"Next birthday: {next_birthday})"
    days_to_birthday = (next_birthday - today).days
    age = (next_birthday - dob).days // 365     # Note, this doesn't take account of leap years so isn't perfect.
    line4=f'Days to next birthday: {days_to_birthday}'
    line5=f'Age at next birthday: {age}'
    return f"{line1, line2, line3, line4, line5}"

app = Flask(__name__)

@app.route('/')
def get_birthday():
    return render_template('birthday_submit_form.html')

@app.route('/birthday', methods=["POST"])
def birthday():
    dob_input = request.form.get('date', '')
    if dob_input:
        try:
            dob = dt.date.fromisoformat(dob_input)
        except ValueError:
            return 'invalid data'
        return calc_next_birthday(dob)
    else:
        return 'no args detected'

@app.route ('/comments', methods=["GET", "POST"])
def show_comments():
    if request.method == "POST":
        comment_input = request.form.get('new_comment', '')
        username = request.form.get('username', '')
        if comment_input and username:
            with open("flask/comments.txt", "a") as file:
                file.write(f"{username}: {comment_input}\n")
        return redirect('/comments')
    comments = []
    with open("flask/comments.txt", "r") as file:
        comments = file.readlines()
    return render_template('comment_box.html', comments=comments)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9008, debug=True)
