class Usuario:

    def __init__(self, name_user, password):
        self.name_user = name_user
        self.password = password

# Crear un objeto Usuario 

user1 = Usuario("user123", "password123")

# Mostrar los detalles del usuario 

print("Detalles del usuario:")
print("Nombre de usuario:", user1.name_user)
print("Contraseña:", user1.password)