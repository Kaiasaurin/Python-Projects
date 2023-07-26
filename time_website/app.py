from flask import Flask, render_template
import datetime 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('clock.html', time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p"))

@app.route('/time')
def time():
    return datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
