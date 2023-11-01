from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ("Hello.html")

@app.route('/rainbow')
def rainbow():
    return render_template ("Rainbow.html")

@app.route('/smile')
def smile():
    return render_template ("Smile.html")

if __name__=="__main__":
    app.run(debug=True)