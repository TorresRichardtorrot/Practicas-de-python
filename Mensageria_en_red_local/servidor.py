import socket
import threading


def handle_cliente(cliente_socket, clien_address):
    while True:
        try:
            #Recibir datos del cliente
            data = cliente_socket.recv(1024).decode("utf-8")
            # print(f"Cliente {clien_address}: {data}")
            
            if data == "exit":
                break
            
            # Enviar una respuesta al cliente
            response = input("Respuesta: ")
            cliente_socket.send(response.encode("utf-8"))
        except Exception as e:
            raise e
    
    cliente_socket.close()        

def run_server():
    # Configurar el servidor 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8000))
    server_socket.listen(5)
    print("Servidor iniciado. Esperando conexiones....")
    
    while True:
        #? Aceptar una conexion
        cliente_socket, client_address = server_socket.accept()
        print(f"Conexion establecida con {client_address}")
        
        # Crear un hilo para manejar el cliente
        cliente_hilo = threading.Thread(target=handle_cliente,args=(cliente_socket, client_address))
        cliente_hilo.start()
        
if __name__ == "__main__":
    run_server()    