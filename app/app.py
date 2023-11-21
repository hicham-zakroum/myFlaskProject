from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # return render_template('home.html', datetoday2=datetoday2)
    return "<h1>Hi from Flask project</h1>"


# @app.route('/count', methods=['GET', 'POST'])
# def count():
#     text = request.form['text']

#     words = len(text.split())

#     paras = replace_multiple_newlines(text)
#     text = text.replace('\r', '')
#     text = text.replace('\n', '')
#     chars = len(text)
#     return render_template('home.html', words=words, paras=paras, chars=chars, datetoday2=datetoday2)


# Our main function which runs the Flask App
if __name__ == '__main__':
    app.run(debug=True)
