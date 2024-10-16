from flask import Flask, render_template, redirect, url_for, request,session

app = Flask(__name__)
app.secret_key = 'unaclavesecreta'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ins")
def ins():
    if 'inscripcion' not in session:
        session['inscripcion'] = []
    return render_template('inscripcionesCursos.html', inscripcion = session['inscripcion'])

@app.route("/procesaInc", methods=['POST'])
def procesaInc():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    curso = request.form.get('curso')
    if 'inscripcion' not in session:
        session['inscripcion'] = []
    session['inscripcion'].append({'nombre': nombre,'apellido':apellido,'curso':curso})
    session.modified = True

    return redirect(url_for('ins'))

@app.route("/vaciarInc")
def vaciarInc():
    # Elimina la session
    session.pop('inscripcion',None)
    return redirect(url_for('ins'))

@app.route("/usu")
def usu():
    if 'usuarios' not in session:
        session['usuarios'] = []
    return render_template('registroUsuarios.html', usuarios = session['usuarios'])

@app.route('/procesaUsu', methods=['POST'])
def procesaUsu():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    email = request.form.get('email')
    contraseña = request.form.get('contraseña')

    if 'usuarios' not in session:
        session['usuarios'] = []
    session['usuarios'].append({'nombre':nombre, 'apellido':apellido, 'email':email, 'contraseña':contraseña})
    session.modified = True

    return redirect(url_for('usu'))

@app.route("/vaciarUsu")
def vaciarUsu():
    # Elimina la session
    session.pop('usuarios',None)
    return redirect(url_for('usu'))

@app.route("/lib")
def lib():
    if 'libros' not in session:
        session['libros'] = []
    return render_template('registroLibros.html', libros = session['libros'])

@app.route('/procesaLib', methods=['POST'])
def procesaLib():
    titulo = request.form.get('titulo')
    autor = request.form.get('autor')
    resumen = request.form.get('resumen')
    medio = request.form.get('medio')

    if 'libros' not in session:
        session['libros'] = []
    session['libros'].append({'titulo':titulo, 'autor':autor, 'resumen':resumen, 'medio':medio})
    session.modified = True

    return redirect(url_for('lib'))

@app.route("/vaciarLib")
def vaciarLib():
    # Elimina la session
    session.pop('libros',None)
    return redirect(url_for('lib'))

@app.route("/pro")
def pro():
    if 'productos' not in session:
        session['productos'] = []
    return render_template('registroProductos.html', productos = session['productos'])

@app.route('/procesaPro', methods=['POST'])
def procesaPro():
    producto = request.form.get('producto')
    categoria = request.form.get('categoria')
    existencia = request.form.get('existencia')
    precio = request.form.get('precio')

    if 'productos' not in session:
        session['productos'] = []
    session['productos'].append({'producto':producto, 'categoria':categoria, 'existencia':existencia, 'precio':precio})
    session.modified = True

    return redirect(url_for('pro'))

@app.route("/vaciarPro")
def vaciarPro():
    # Elimina la session
    session.pop('productos',None)
    return redirect(url_for('pro'))

if __name__ == '__main__':
    app.run(debug=True)