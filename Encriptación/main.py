from cryptography.fernet import Fernet

# * cryptography.fernet es un módulo de la biblioteca de Python llamada "cryptography"
# * que se utiliza para trabajar con el cifrado Fernet. Fernet es un esquema de cifrado
# * simétrico que proporciona autenticación y protección contra manipulación de datos.
# * Es particularmente útil para cifrar y descifrar datos sensibles o secretos.


def generar_clave():
    return Fernet.generate_key()


def encriptar_texto(texto, clave):
    f = Fernet(clave)
    texto_encriptado = f.encrypt(texto.encode())
    return texto_encriptado


def desencriptar_texto(texto_encriptado, clave):
    f = Fernet(clave)
    texto_encriptado = f.decrypt(texto_encriptado).decode()
    return texto_encriptado


#!generar una clave secreta
clave_secreta = generar_clave()

#!Texto a encriptar
texto_original = "Texto a encriptar"

#!Ecriptar
texto_encriptado = encriptar_texto(texto_original, clave_secreta)

print("*"*100)
print(f"texto original: {texto_original}")
print("*"*100)
print(f"texto encriptado: {texto_encriptado}")
print("*"*100)

#! Desencriptar el Texto
texto_desencriptado = desencriptar_texto(texto_encriptado, clave_secreta)

print(f"Texto Desencriptado: {texto_desencriptado}")
print("*"*100)
