from flask import Flask, render_template
from flask_apscheduler import APScheduler

from news_parser import launch

app = Flask(__name__)
scheduler = APScheduler()


@app.route('/')
def index():
    return render_template('index.html', news=launch())


if __name__ == '__main__':
    scheduler.add_job(id='Get news', func=launch, trigger='interval', seconds=3600)
    scheduler.start()
    app.run(debug=True)