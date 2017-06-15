from flask import Flask, render_template
import newslogdb

app = Flask(__name__)


@app.route('/')
def hello_world():
    all_atricles = newslogdb.articles()
    all_authors = newslogdb.authors()
    all_errors = newslogdb.all()

    return render_template('index.html',title='Log Dashboard',
                           all_articles = all_atricles,
                           all_authors = all_authors,
                           all_errors=all_errors)


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=8080)
