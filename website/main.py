from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def page():
    return render_template('main.html')

@app.route('/phone')
def phone():
    return render_template('phone.html')

@app.route('/email_form')
def email_form():
    return render_template('email_form.html')

@app.route('/text')
def text():
    return render_template('text.html')

@app.route('/tty')
def tty():
    return render_template('tty.html')

@app.route('/email')
def email():
    return render_template('email.html')

@app.route('/relay')
def relay():
    return render_template('relay.html')

@app.route('/phone2')
def phone2():
    return render_template('phone2.html')

@app.route('/email_form2')
def email_form2():
    return render_template('email_form2.html')

@app.route('/text2')
def text2():
    return render_template('text2.html')

@app.route('/tty2')
def tty2():
    return render_template('tty2.html')

@app.route('/email2')
def email2():
    return render_template('email2.html')

@app.route('/relay2')
def relay2():
    return render_template('relay2.html')

@app.route('/forbidden')
def forbidden():
    return render_template('forbidden.html')

@app.route('/not_found')
def not_found():
    return render_template('not_found.html')

@app.route('/cant_decode')
def cant_decode():
    return render_template('cant_decode.html')

@app.route('/javascript')
def javascript():
    return render_template('javascript.html')

@app.route('/bad_website')
def bad_website():
    return render_template('bad_website.html')
    
if __name__ == "__main__":
    app.run(debug=True)
