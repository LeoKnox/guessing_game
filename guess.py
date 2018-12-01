from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'make it so number one'

@app.route('/')
def guessing_game():
    #session.clear();
    if 'mynum' not in session:
        for x in range (10):
            session['mynum'] = random.randint(1, 100)
    return render_template('guess.html')

@app.route('/again', methods=['POST'])
def try_again():
    if int(request.form['answer']) == session['mynum']:
        session['judge']='Correct'
        session['lohi']=''
        session.clear();
    else:
        session['judge']='WronG!'
        if int(request.form['answer'])>session['mynum']:
            session['lohi'] = "You reached too high!"
        else:
            session['lohi'] = "Too low!"
    return redirect('/')
    

if __name__=="__main__":   
    app.run(debug=True) 
