
##Jinja2 template engine
'''
{%...%} conditions,for loops
{{    }} expressions to print output
{#....#} this is for comments
'''
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcom():
    return render_template('index2.html')

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = 'FAIL'
    exp = {'score': score, 'res': res}
    return render_template('results.html', result=exp)

@app.route('/failure/<int:score>')
def failure(score):
    return "The Person has failed and the marks is "+ str(score)

@app.route('/results/,int:marks>')
def results(marks):
    results = ""
    if marks < 50:
        results = 'failure'
    else:
        results = 'success'
    return redirect(url_for(results, score=marks))

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science + maths + c + data_science)/4
    result = ""
    if total_score >= 50:
        result = 'success'
    else:
        result = "failure"
    return redirect(url_for(result, score=total_score))


if __name__ == '__main__':
    app.run(debug=True)