import os

from flask import Flask, render_template, redirect, url_for, request
from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy

from news_parser import launch

from forms import Newsform

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:19734682@localhost/dummy'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.secret_key = "ghfs8119hffd91jr10rhf810"
scheduler = APScheduler()

db = SQLAlchemy(app)


@app.route('/')
def index():
    from models import News
    user_news = News.query.all()
    return render_template('index.html', news=launch(), user_news=user_news)


@app.route('/add_news', methods=["GET", "POST"])
def add_news():
    form = Newsform()
    if request.method == "POST":
        from models import News

        if form.validate_on_submit():
            new_topic = News(form.header.data, form.body.data)
            db.session.add(new_topic)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            print('Something went wrong!')
            return redirect(url_for('index'))
    else:
        return render_template('news_form.html', form=form)


if __name__ == '__main__':
    scheduler.add_job(id='Get news', func=launch, trigger='interval', seconds=3600)
    scheduler.start()
    db.create_all()
    app.run(debug=True)