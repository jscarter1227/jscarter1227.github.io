from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('index.html')

@app.route("/index.html")
def hello2():
  return render_template('index.html')

@app.route("/temp")
def temp():
  return "This is a temperature place holder."

if __name__ == "__main__":
  app.run(debug = True, host = '0.0.0.0')
