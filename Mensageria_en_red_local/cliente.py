import socket

def run_cliente():
    # Conectarnos al servidor
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(("localhost", 8000))
    print("Conectado al servidor")

    while True:
        # Enviar un mensaje al servidor
        message = input("Mensaje: ")
        cliente_socket.send(message.encode('utf-8'))

        if message == "exit":
            break

        # Recibir la respuesta del servidor
        response = cliente_socket.recv(1024).decode('utf-8')
        print("Servidor:", response)

    cliente_socket.close()

if __name__ == "__main__":
    run_cliente()
