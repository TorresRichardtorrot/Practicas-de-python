import subprocess
nombre_wifi = "¥Torres¥_5G"

result = subprocess.run([
    "netsh","wlan","show","profile", nombre_wifi,"key=clear"],
    stdout=subprocess.PIPE,
)
salida = result.stdout.decode("latin1")

for linea in salida.split("\n"):
    # print(linea)
    if "key Content" in linea or "Contenido de la clave" in linea:
        print("La contraseña de la red es: ", linea.split(":")[1].strip())