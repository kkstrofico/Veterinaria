# Importamos el módulo 'sys' para acceder a las configuraciones del sistema
import sys  

# Añadimos la ruta de la carpeta que contiene el archivo 'bsd.py' a 'sys.path'.
# Esto le dice a Python que busque en esta carpeta cuando intentamos importar módulos.
sys.path.append((r'C:\Users\hp\OneDrive\Documentos\Veterinaria Repositorio\Veterinaria\src'))  

# Ahora, importamos el módulo 'bsd' desde la carpeta que acabamos de añadir a 'sys.path'.
# Python buscará 'bsd.py' en la ruta especificada y lo cargará.
import bsd  
class Mascota: # clase mascota, que se encarga de recopilar la informacion de la mascota y subirla a la lista mascota
    def __init__(self, id="", nombre="", color="", especie="",raza="No aplica",veterinario=""): # parametros que recibe la mascota
        self.id = id
        self.nombre = nombre 
        self.color = color 
        self.especie = especie
        self.raza = raza
        self.veterinario = veterinario
    def registrar_mascota(self): # metodo de la mascota que permitira almacenar los datos de la mascota en un diccionario
        diccionario_mascota={
            "Id":self.id,
            "Nombre": self.nombre,
            "Color": self.color,
            "Especie":self.especie,
            "Raza":self.raza,
            "Veterinario":self.veterinario
        }
        bsd.ides_mascotas.append(self.id) # se almacenara en la lista ides_mascotas el id de la mascota actual
        bsd.lista_mascota.append(diccionario_mascota) # se almacenara el diccionario con toda la información de la mascota a la lista que contiene todas las informaciones de las mascotas
        
    