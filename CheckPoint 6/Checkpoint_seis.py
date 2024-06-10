class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

    def mostrar_info(self):
        print(f'Nombre de usuario: {self.nombre_usuario}')
        
        print(f'Contraseña: {self.contrasena}')


usuario_uno = Usuario("Borja", "123456789")


usuario_uno.mostrar_info()
