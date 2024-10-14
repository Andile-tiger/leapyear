from flask import Flask, render_template, request

app = Flask(__name__)

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

@app.route('leap.html', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        year = int(request.form['year'])
        result = is_leap_year(year)
        if result:
            result = f"{year} is a leap year."
        else:
            result = f"{year} is not a leap year."
        return render_template('leap.html', result=result)
    else:
        return render_template('leap.html')

if __name__ == '__main__':
    app.run(debug=True)