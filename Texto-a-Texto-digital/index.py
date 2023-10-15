from PIL import Image
#* PIL, o "Python Imaging Library," fue una biblioteca de Python popular utilizada
#* para el procesamiento de imágenes y manipulación de gráficos. Sin embargo,
#* PIL dejó de recibir actualizaciones significativas y se considera obsoleto.
#* En su lugar, se recomienda el uso de la biblioteca "Pillow."

import pytesseract
#* pytesseract es una biblioteca de Python que proporciona una interfaz para utilizar el motor
#* OCR (Optical Character Recognition) de Tesseract. OCR es una tecnología que se utiliza para reconocer
#* texto a partir de imágenes o escaneos. Tesseract es uno de los motores OCR de código abierto más populares
#* y ampliamente utilizados.



pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

ruta_imagen = "img.jpg"
imagen_abierta = Image.open(ruta_imagen)
texto = pytesseract.image_to_string(imagen_abierta)
print(texto)