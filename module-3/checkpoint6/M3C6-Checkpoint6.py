class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

# Crear un objeto de la clase User 

user = User("user123", "password123")

# Imprimir el nombre de usuario y la contraseña

print(f"Nombre de usuario: {user.username}")
print(f"Contraseña: {user.password}")