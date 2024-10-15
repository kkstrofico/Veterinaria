class Propietario: #clase propietario que contiene la informacion del propietario que se va a pedir
    def __init__(self,id, nombres, apellidos, direccion, telefono, correo, mascota): #sus atributos
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.mascota = mascota