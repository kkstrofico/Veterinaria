import bsd
class Veterinario:#Clase Veterinario
    def __init__(self,id,nombres,apellidos,direccion,telefono,tarjeta):#Todos sus atributos
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.telfono = telefono
        self.tarjeta = tarjeta
        pass
    def registrar_veterinario(self):
        diccionario_veterinario = {
            "id":self.id,
            "nombres":self.nombres,
            "apellidos":self.apellidos,
            "direccion":self.direccion,
            "telefono":self.telfono,
            "tarjeta profesional":self.tarjeta
        }
        bsd.ides_veterinarios.append(self.id)#Se guardardo el id del veterinario a la lista respectiva
        bsd.lista_veterinarios.append(diccionario_veterinario) #Se subio a la 
    def tarjeta_profesional(self):#MEtodo que solicita la tarjeta profesional
        pass