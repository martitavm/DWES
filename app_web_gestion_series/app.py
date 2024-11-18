from flask import Flask, render_template, session, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_python_mejor_lenguaje'

usuarios = {}
datos_serie = {}
CATEGORIES = ["Series que me gustarían ver", "Series que estoy viendo", "Series vistas"]
@app.route('/')
def home():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    series_usuario = datos_serie.get(session['usuario'], {categoria: [] for categoria in CATEGORIES})

    return render_template('home.html', user=session['usuario'], series=series_usuario)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in usuarios and usuarios[username] == password:
            session['usuario'] = username
            return redirect(url_for('home'))
        else:
            error = "Credenciales incorrectas, vuelve a intentarlo"
            return render_template('login.html', error=error)

    if not usuarios:
        return redirect(url_for('registrar'))

    return render_template('login.html')


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in usuarios:
            flash('El usuario ya está registrado.')
        else:
            usuarios[username] = password  # Guardamos el usuario y su contraseña
            datos_serie[username] = {category: [] for category in CATEGORIES}  # Inicializamos sus series
            return redirect(url_for('login'))

    return render_template('registrar.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

@app.route('/add_serie', methods=['GET', 'POST'])
def add_serie():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
            categoria = request.form['categoría']

            nueva_serie = {
                "nombre": request.form['nombre'],
                "sinopsis": request.form['sinopsis'],
                "puntuación": float(request.form['puntuación']),
                "género": request.form['género'],
                "fecha_estreno": request.form['fecha_estreno'],
                "número_capítulos": int(request.form['número_capítulos']),
                "duración_capítulos": int(request.form['duración_capítulos']),
            }
            datos_serie[session['usuario']][categoria].append(nueva_serie)
            return redirect(url_for('home'))

    return render_template('add_serie.html', categories=CATEGORIES)

if __name__ == '__main__':
    app.run()

