from flask import render_template, request, session
from app import app

@app.route('/')
@app.route('/getform')
def get_and_display_form():
    return render_template('index.html',
                           the_title="This is the index page", )


@app.route('/processform', methods=['POST'])
def process_the_form():
    global guitarist
    global why
    session['guitarist'] = request.form['hero']
    session['why'] = request.form['why']
    return render_template('guitarist.html',
                           the_title="Here are your results",
                           the_hero=session['guitarist'],
                           the_why=session['why'], )


@app.route('/fabfour')
def beatles():
    names = 'John Paul George Ringo'.split()
    return render_template('fabfour.html',
                           the_title="Say hello to the Fab Four",
                           the_names=names, 
                           the_guitarist=session.get('guitarist', 'unknown'),
                           the_why=session.get('why', 'unknown'), )