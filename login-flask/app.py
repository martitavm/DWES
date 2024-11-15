from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key = 'clave_secreta_muerte_a_javascript'
USERNAME = 'martita'
PASSWORD = 'supersecret-password'

@app.route('/')
def home():
        return render_template('home.html',logged_in=session.get('logged_in'), username=session.get('username'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #Validacion de credenciales
        username = request.form.get('username')
        password = request.form.get('password')

        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('home'))
        else:
            error = "credenciales incorrectas, vuelve a intentarlo"
            return render_template('login.html', error=error)

    return render_template('login.html')

if __name__ == '__main__':
    app.run()
