from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', endpoint='home')
def index():
   return render_template('inicio/inicio.html')

@app.route('/quienes_somos')
def quienes_somos():
   return render_template('quienes_somos/quienes_somos.html')

@app.route('/servicios')
def servicios():
   return render_template('servicios/servicios.html')

@app.route('/noticias')
def noticias():
   return render_template('noticias/noticias.html')

@app.route('/contacto')
def contacto():
   return render_template('contacto/contacto.html')

if __name__ == '__main__':
    app.run(debug=True)