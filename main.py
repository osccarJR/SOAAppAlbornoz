import threading
from producer import send_message
from consumer import consume_message

# Crear un hilo para el consumidor
consumer_thread = threading.Thread(target=consume_message)
consumer_thread.start()

# Enviar un mensaje desde el productor
message = "Hola, este es un mensaje de prueba por correo electrónico"
send_message(message)

# Esperar a que el consumidor termine
consumer_thread.join()
