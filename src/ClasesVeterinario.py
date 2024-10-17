import ClasseMascota 
import ClassePropietario
import bsd
class Veterinario:#Clase Veterinario
    def __init__(self,id = "",nombres = "",apellidos ="",direccion ="",telefono ="",tarjeta=""):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.tarjeta = tarjeta
        
    def registrar_veterinario(self):
        diccionario_veterinario = {
            "Id":self.id,
            "nombres":self.nombres,
            "apellidos":self.apellidos,
            "direccion":self.direccion,
            "telefono":self.telefono,
            "tarjeta profesional":[self.tarjeta],
            "Mascotas":[]
        }
        bsd.ides_veterinarios.append(self.id)#Se guardardo el id del veterinario a la lista respectiva
        bsd.lista_veterinarios.append(diccionario_veterinario) #Se subio a la lista de veterinarios
        
    def registrar_mascota(self):
        #Solicitar datos propietario
        print("\nINGRESAR DATOS PROPIETARIO\n")
        id = input("ID: "),
        nombre=input("NOMBRE: "),
        apellido = input("APELLIDOS: "),
        direccion = input("DIRECCION: "),
        telefono = input("TELEFONO: "),
        correo = input("CORREO: ")
        propietario = ClassePropietario.Propietario(id,nombre,apellido,direccion,telefono,correo)
        #Solicitar datos de la mascota 
        print("\nINGRESA LOS DATOS DE LA MASCOTA\n")
        nombre=input("Nombre:").lower()
        especie=input("Especie: ")
        mascota_existe = verificar_mascota_existente(nombre,especie)
        print(mascota_existe)
        #No dejar pasar si estos dos datos ya existen
        while mascota_existe == True:
            print("La mascota ya existe")
            nombre=input("Nombre:")
            especie=input("Especie: ")
        mascota = ClasseMascota.Mascota("131313",nombre = nombre,color=input("Color: "),especie=especie, raza=input("Raza: "))
        #Guardar datos de la mascota y el propietario en la lista 
        propietario.registrar_propietario()
        mascota.registrar_mascota()
        
    def buscar_mascota(self):#Metodo para buscar una mascota en especifico
        mascota_buscar = input('Ingresa el nombre de la mascota que deseas buscar: ').lower() # se solicita el nombre de la mascota que se desea buscar
        for i in bsd.lista_mascota: 
            if i['Nombre'] == mascota_buscar: # se verifica que el nombre se encuentre
                print(i) # se imprime todos los diccionarios de las mascotas que tengan ese nombre
        while True:
            mascota_buscar_id = input('Ingresa el ID de la mascota: ') # Se solicita el numero de ID de la mascota
            #Excepciones
            if mascota_buscar_id.isnumeric()==False:
                print("Error, ingresa numeros")
            elif len(mascota_buscar_id) != 4:
                print("Error, ingresa 4 digitos")
            elif mascota_buscar_id not in bsd.ides_mascotas:
                print('El id ingresado no existe\n asegurare de haber escrito correctamente.')
            else:
                break
        # se imprime el diccionario que corresponde al id ingresado
        for i in bsd.lista_mascota:
            if i['Id'] == mascota_buscar_id:
                print(i)
                
                
    def buscar_mascotas(self): # metodo que muestra todas las mascotas
        print('LISTA MASCOTAS')
        for i in bsd.lista_mascota:
            print(f"{i.values()}\n")



    def tarjeta_profesional(self):#Metodo que solicita la tarjeta profesional de veterinario
        print(f"\t\n TARJETA PROFESIONAL\n")
        diccionario_tarjeta={ # diccionario con toda la información de la tarjeta profesional
            "Nombre":f"{self.nombres} {self.apellidos}",
            "Nombre Titulo":"",
            "Nombre Especialidad":"",
            "Nombre instituto":"",
            "Año":""
        }
        while True: 
            especialidad=input("Ingresa la especialidad: ").strip()
            if especialidad.isalpha()==False:
                print("Error, ingresa solo str")
            else:
                break
            
        while True: 
            nombre_instituto=input("Ingresa el nombre del instituto: ").strip()
            if nombre_instituto.isnumeric()==True:
                print("Error, ingresa solo str")
            else:
                break
            
        while True: 
            Año=input("Ingresa el año de certificación: ").strip()
            if Año.isnumeric()==False:
                print("Error, ingresa solo numeros")
            else:
                break
        while True: 
            nombre_titulo=input("Ingresa el titulo: ").strip()
            if nombre_titulo.isalpha()==False:
                print("Error, ingresa solo str")
            else:
                break
        diccionario_tarjeta["Nombre Titulo"]=nombre_titulo
        diccionario_tarjeta["Nombre Especialidad"]=especialidad
        diccionario_tarjeta["Nombre instituto"]=nombre_instituto
        diccionario_tarjeta["Año"]= Año
        return diccionario_tarjeta
    
def verificar_mascota_existente(nombre,especie):#Verifica si una mascota existe o no
    #Recorrer la lista de mascotas para verificar comparar si la mascota existe o no 
    for i in bsd.lista_mascota:
        if i["Nombre"]==nombre: 
            return True
        elif i["Especie"]== especie:
            return True
        else: 
            return False
#Veterinario().buscar_mascotas()
#Veterinario().buscar_mascota()
