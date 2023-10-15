from stegano import lsb
from PIL import Image

#*pip install stegano

def ocultar_info(imagen_path):
    #Abrir imagen 
    img = Image.open(imagen_path)
    mensaje = "Hola, gracias por todo"
    
    # Ocultar el mensaje en la imagen
    imagen_oculta = lsb.hide(img,mensaje)
    
    #guardar mensaje
    return imagen_oculta.save("imagen_con_mensaje.png")

def recuperar_info(imagen_oculta_path):
     #Abrir imagen 
    img = Image.open(imagen_oculta_path)
    
    # Recuperar el mensaje
    mensaje_recuperado = lsb.reveal(imagen_oculta_path)
    print(mensaje_recuperado)
    
    


recuperar_info("imagen_con_mensaje.png")