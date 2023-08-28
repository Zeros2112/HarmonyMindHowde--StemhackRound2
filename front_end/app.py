from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def about():
    return render_template('homepage.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/chatbot')
def chatbottt():
    return render_template('base.html')

@app.route('/diary')
def note():
    return render_template('note.html')

@app.route('/friends')
def friendssss():
    return render_template('friends.html')

@app.route('/movies')
def moviesss():
    return render_template('movies.html')

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/sleep')
def sleep():
    return render_template('sleep.html')



if __name__ == '__main__':
    app.run(debug=True)