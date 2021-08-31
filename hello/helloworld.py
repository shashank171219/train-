from flask import Flask, render_template

app=Flask(__name__,template_folder='template')


@app.route('/')
def index():
    return render_template('web1.html')

app.run(host='0.0.0.0', port=85)