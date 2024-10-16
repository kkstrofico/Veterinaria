import ClasseMascota 
import ClassePropietario
import bsd
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
    def registrar_propietario(self):
        #Solicitar datos propietario
        print("\nINGRESAR DATOS PROPIETARIO\n")
        id = input("ID: "),
        nombre=input("NOMBRE: "),
        apellido = input("APELLIDOS: "),
        direccion = input("DIRECCION: "),
        telefono = input("TELEFON: "),
        correo = input("CORREO: ")
        propietario = ClassePropietario.Propietario(id,nombre,apellido,direccion,telefono,correo)
        #Solicitar datos de la mascota 
        print("\nINSGRESA LOS DATOS DE LA MASCOTA\n")
        nombre=input("Nombre:")
        especie=input("Especie: ")
        mascota_existe = verificar_mascota_existente(nombre,especie)
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
    def buscar_mascota(self):#Metodo para buscar una mascota en especifico
        mascota_buscar = input('Ingresa el nombre de la mascota que deseas buscar: ')
        for i in bsd.lista_mascota:
            if i['Nombre'] == mascota_buscar:
                print(i)
        mascota_buscar_id = input('Ingresa el ID de la mascota: ')
        while mascota_buscar_id not in bsd.ides_mascotas:
            print('El id ingresado no existe\n asegurare de haber escrito correctamente.')
            mascota_buscar_id = input('Ingresa el ID de la mascota: ')
        for i in bsd.lista_mascota:
            if i['ID'] == mascota_buscar_id:
                print(i)
    def buscar_mascotas(self):
        print('LISTA MASCOTAS')
        for i in bsd.lista_mascota:
            print(f"{i.values()}\n")

    def tarjeta_profesional(self):#Metodo que solicita la tarjeta profesional
        pass
def verificar_mascota_existente(nombre,especie):#Verifica si una mascota existe o no
    #Recorrer la lista de mascotas para verificar comparar si la mascota existe o no 
    for i in bsd.lista_mascota:
        if nombre == i["Nombre"] and i["Especie"] == especie:
            return True
        else: 
            return False
Veterinario().registrar_propietario()   
Veterinario().buscar_mascota()
