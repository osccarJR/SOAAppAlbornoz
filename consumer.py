import queue
import smtplib
from email.mime.text import MIMEText

# Crear una cola
message_queue = queue.Queue()

# Función para enviar correos 
def send_email(body):
    sender_email = "your_email@example.com"
    receiver_email = "receiver@example.com"
    password = "your_password"

    msg = MIMEText(body)
    msg['Subject'] = 'Test Email'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"Email sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Funcion para recibir mensajes de la cola y enviarlos por correo 
def consume_message():
    while True:
        if not message_queue.empty():
            message = message_queue.get()
            print(f"Received message: {message}")
            send_email(message)

if __name__ == "__main__":
    consume_message()
