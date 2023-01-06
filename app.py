from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hellohtml():
    return render_template("hello.html")

@app.route('/kospi')
def kospihtml():
    result = "kospi page"
    return render_template("kospi.html", result=result)

@app.route('/nasdaq')
def nasdaqhtml():
    result = "nasdaq page"
    return render_template("nasdaq.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
