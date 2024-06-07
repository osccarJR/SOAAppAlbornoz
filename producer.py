import queue

# Crear una cola
message_queue = queue.Queue()

# Función para enviar un mensaje a la cola
def send_message(message):
    message_queue.put(message)
    print(f"Message sent: {message}")

if __name__ == "__main__":
    message = "Hola, este es un mensaje de prueba por correo electronico"
    send_message(message)
