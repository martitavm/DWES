from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    # Verificar si el usuario ya aceptó o rechazó las cookies
    user_cookie = request.cookies.get('cookies_accepted')

    # Si el usuario ha decidido sobre las cookies, mostramos la página principal
    if user_cookie == 'True':
        return render_template('index.html')
    # Si el usuario ha rechazado las cookies, lo redirigimos al banner
    elif user_cookie == 'False':
        return render_template('cookie_banner.html')
    # Si el usuario no tiene decisión, mostramos el banner
    else:
        return render_template('cookie_banner.html')


# Ruta para aceptar cookies
@app.route('/accept_cookies', methods=['POST'])
def accept_cookies():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('cookies_accepted', 'True', max_age=3600, httponly=True, secure=True)
    return response


# Ruta para rechazar cookies
@app.route('/reject_cookies', methods=['POST'])
def reject_cookies():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('cookies_accepted', 'False')
    return response

@app.route('/politicas_cookies')
def politicas_cookies():
    return render_template('politicas_cookies.html')


if __name__ == '__main__':
    app.run(debug=True)




