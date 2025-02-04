from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/Nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/Servicios')
def servicios():
    return render_template('servicios.html')


# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Cambia esto si usas otro servidor SMTP
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'abtrujilloyasociados@gmail.com'  # Tu correo electrónico
app.config['MAIL_PASSWORD'] = 'ktum nzxk roff itwu'  # Tu contraseña
app.config['MAIL_DEFAULT_SENDER'] = ('Trujillo y Asociados', 'abtrujilloyasociados@gmail.com')

mail = Mail(app)

@app.route('/send-email', methods=['POST'])
def send_email():
    # Obtener datos del formulario
    name = request.form.get('name')
    email = request.form.get('email')
    telefono = request.form.get('telefono')
    message = request.form.get('message')

    if not all([name, email, telefono, message]):
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400

    # Crear y enviar el correo
    try:
        msg = Message(
            subject=f"Nuevo mensaje de {name}",
            recipients=['abtrujilloyasociados@gmail.com'],  # Cambia al correo del destinatario
            body=f"Nombre: {name}\nTeléfono: {telefono}\nCorreo: {email}\nMensaje:\n{message}"
        )
        mail.send(msg)
        return jsonify({'success': 'Correo enviado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
