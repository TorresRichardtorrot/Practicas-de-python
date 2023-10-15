import sqlite3

# ? Conexion a la base de datos

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# ? Crear tabla si no a sido creada

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    email TEXT
    ) """
)


conn.commit()

# ? Crear registro


def crear_usuario(nombre: str, email) -> str:
    cursor.execute(
        "INSERT INTO usuarios(nombre,email) VALUES(?,?)", (nombre, email))
    conn.commit()
    print("Usuario Agregado")


# ?Actualiza usuario por id
def actualizar_usuario(id: int, nombre: str, email: str) -> str:
    cursor.execute(
        "UPDATE usuarios SET nombre=?, email=? WHERE id=?", (nombre, email, id))
    conn.commit()
    return "Usuario actualizado"


# ? Obtener registros
def obtener_usuarios() -> list:
    cursor.execute("SELECT id,nombre,email FROM usuarios ")
    usuarios = cursor.fetchall()

    lista_usuarios = []
    for usuario in usuarios:
        lista_usuarios.append(usuario)

    return lista_usuarios

# ? Eliminar usuario


def eliminar_usuario(id):
    cursor.execute("DELETE FROM usuarios WHERE id = ? ", (id,))
    conn.commit()
    return "Usuario eliminado"


# ? Leer registro por id
def obtener_usuario(id: int) -> list:
    cursor.execute("SELECT id,nombre,email FROM usuarios WHERE id = ? ", (id,))
    usuario = cursor.fetchone()

    if usuario:
        return usuario
    return "Usuario no encontrado"

#! Craer usuario

# crear_usuario("daniel","daniel@example.com")
# crear_usuario("pedro","pedro@example.com")
# crear_usuario("carlos","carlos@example.com")

#! Obtener todos los ususarios registrados
# print(obtener_usuarios())

#!actualizar usuario
# print(actualizar_usuario(2,"mimo","null"))

#!obtener usuario
# print(obtener_usuario(4))


#!Eliminar usuario
# print(eliminar_usuario(2))
