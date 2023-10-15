# pip install rembg

from rembg import remove
from PIL import Image


quitar_fondo = remove(Image.open("gatito.png"))
quitar_fondo.save("imagen_sin_fondo.png")