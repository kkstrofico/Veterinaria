import bsd
class Propietario: #clase propietario que contiene la informacion del propietario que se va a pedir
    def __init__(self,id="", nombres="", apellidos="", direccion="", telefono="", correo="", mascota=""): #sus atributos
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.mascota = mascota
    def registrar_propietario(self): #metodo del propietario que permitira almacenar los datos del propietario en un diccionario
        diccionario_propietario={
            "ID":self.id,
            "Nombre":self.nombre,
            "Apellidos":self.apelidos,
            "Direccion":self.direccion,
            "Telefono":self.telefono,
            "Correo":self.correo,
            "Mascota":self.mascota
        }
        bsd.ides_propietarios.append(self.id) #se almacenara en la lista ides_propietarios el id del propietario
        bsd.lista_propietario.append(diccionario_propietario) #se almacenara el diccionario con toda la informacion del propietario a la lista que contiene todas las informaciones del propietario
