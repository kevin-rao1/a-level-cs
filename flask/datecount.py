from flask import Flask
from flask import request
from flask import render_template
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
def get_name():
    return render_template('birthday_submit_form.html')

@app.route('/birthday', methods=["POST"])
def birthday():
    year = request.form.get('year', '')
    month = request.form.get('month', '')
    day = request.form.get('day', '')
    if year and month and day:
        try:
            dob = dt.date(int(year), int(month), int(day))
        except ValueError:
            return 'invalid data'
        return calc_next_birthday(dob)
    else:
        return 'no args detected'



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9008, debug=True)
