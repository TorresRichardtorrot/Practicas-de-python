
import cv2


#? Especificar la ruta de la imagen a dibujo

imagen = cv2.imread("thor.jpg")
nombre_ventana = "Imagen Original"

#? Mostrar la imagen original en una ventana
cv2.imshow(nombre_ventana,imagen)


#?convertir la imagen de un color a otro
img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
color_invertido = cv2.bitwise_not(img_gris)

#? Suavizar la imagen 
desenfoque = cv2.GaussianBlur(color_invertido,(101,101),0)
desenfoque_invertido = cv2.bitwise_not(desenfoque)
dibujo = cv2.divide(img_gris, desenfoque_invertido, scale=256.0)


#? guardar la imagen convertida
cv2.imwrite("imagen-en-dibujo.png", dibujo)

#? Leer la imagen nueva
imagen = cv2.imread("imagen-en-dibujo.png")

#? Nombre de la ventana dibujo 
nombre_ventana = "Imagen dibujo"

#? Mostrar la imagen original en una ventana 
cv2.imshow(nombre_ventana, imagen)


#?esperar a que el usuari presione una tecla , para evitar que el kernel del Python se bloqueé
cv2.waitKey(0)

#? Cerrar ventanas
cv2.destroyAllWindows()