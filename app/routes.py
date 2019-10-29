from app import app
from flask import render_template, url_for, redirect
from app.forms import ContactForm


@app.route('/')
@app.route('/index')
def index():


    return render_template('index.html', title='Who We Are')

@app.route('/what_we_do')
def what_we_do():


    return render_template('what_we_do.html', title='What We Do')



@app.route('/where_we_work')
def where_we_work():


    return render_template('where_we_work.html', title='Where We Work')


@app.route('/news_and_events')
def news_and_events():


    return render_template('news.html', title='News & Events')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():

        return redirect(url_for('index'))

    return render_template('contact.html', form=form, title='Contact Us')
