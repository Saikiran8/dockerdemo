from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
    print("Hello World")
    #return "Hello World!"
    return render_template('index.html')

@app.route("/1")
def hello1():
    print("You've done it")
    return "You've done it"
#
# if __name__ == "__main__":
app.run(host='0.0.0.0')