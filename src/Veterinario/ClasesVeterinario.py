import Veterinaria.src.bsd as bsd 
from Propietario_Mascota import ClasseMascota,ClassePropietario
class Veterinario:#Clase Veterinario
    def __init__(self,id = "",nombres = "",apellidos ="",direccion ="",telefono ="",tarjeta =""):#Todos sus atributos
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
        bsd.lista_veterinarios.append(diccionario_veterinario) #Se subio a la lista de veterinarios
    def registrar_mascota(self):
        #Solicitar datos propietario
        propietario = ClassePropietario(id = input("ID: "),nombre=input("NOMBRE: "),apellido = input("APELLIDOS: "),direccon = input("DIRECCION: "),telefono = input("TELEFON: "),correo = input("CORREO: "))
        #Solicitar datos de la mascota 
        nombre=input("Nombre:")
        especie=input("Especie: ")
        mascota_existe = verificar_mascota_existente()
        #No dejar pasar si estos dos datos ya existen
        while mascota_existe == True:
            print("La mascota ya existe")
            nombre=input("Nombre:")
            especie=input("Especie: ")
        mascota = ClasseMascota.Mascota(nombre = nombre,color=input("Color"),especie=especie, raza=input("Raza: "))
        propietario.mascota = mascota.id
        #Guardar datos de la mascota y el propietario en la lista 
        propietario.registrar_propietario()
        mascota.registrar_mascota()
    def tarjeta_profesional(self):#Metodo que solicita la tarjeta profesional
        pass
def verificar_mascota_existente(nombre,especie):#Verifica si una mascota existe o no
    #Recorrer la lista de mascotas para verificar comparar si la mascota existe o no 
    for i in bsd.lista_mascota:
        if nombre == i["Nombre"] and i["Especie"] == especie:
            return True
        else: 
            return False
veterinario = Veterinario()
veterinario.registrar_mascota()
