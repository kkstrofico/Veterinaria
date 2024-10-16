# Importamos el módulo 'sys' para acceder a las configuraciones del sistema
import sys  

# Añadimos la ruta de la carpeta que contiene el archivo 'bsd.py' a 'sys.path'.
# Esto le dice a Python que busque en esta carpeta cuando intentamos importar módulos.
sys.path.append((r'C:\Users\hp\OneDrive\Documentos\Veterinaria Repositorio\Veterinaria\src'))  

# Ahora, importamos el módulo 'bsd' desde la carpeta que acabamos de añadir a 'sys.path'.
# Python buscará 'bsd.py' en la ruta especificada y lo cargará.
import bsd  
def asignar(): # funcion que se encargara de asignar un veterinario a una mascota, y una mascota a un veterinario
    while True:
        id_veterinario = input("Ingresa el id veterinario: ") # solicitar id del veterinario
        if len(id_veterinario) !=10: # excepcion
            print("Error, ingresa 10 digitos")
        elif id_veterinario.isnumeric()== False: # Si el id_veterinario no es numerico
            print("Error, ingresa numeros")
        elif id_veterinario not in bsd.ides_veterinarios: # si el id no se encuentra en la lista ides_veterinarios
            print("Error, ese id no se encuentra registrado.")
        else: # finalizar bucle
            break
    for i in bsd.lista_veterinarios: # recorrer lista que contiene los diccionarios de todos los veterinarios
        if i["id"]== id_veterinario: # se compara si el id que se encuentra en este es igual al id que fue ingresado
            print("\n INGRESA EL ID DE LA MASCOTA\n")
            mascotas_sin_veterinario=[] # id de mascotas que no tienen veterinario
            for j in bsd.lista_mascota: # un for que iterara sobre las mascotas y mostrara las que ya no tienen veterinario
                if j["Veterinario"]==0:
                    mascotas_sin_veterinario.append(j["id"])
            print(f"\n MASCOTAS SIN VETERINARIO\n {mascotas_sin_veterinario}")
            while True:
                id_mascota= input("Ingresa el id de la mascota: ") # se solicita el numero de id de la mascota
                if len(id_mascota) != 4:
                    print("El id de la mascota es de 4 digitos")
                elif id_mascota not in bsd.ides_mascotas: # si el numero de ficha no se encuentra en la lista ides_mascotas
                    print("Error, ese id no se encuentra")
                elif id_mascota.isnumeric()==False:
                    print("Error, ingresa numeros")
                elif id_mascota in i["Mascotas"]: # si el id de la mascota ya esta asignada al veterinario
                    print("Este veterinario ya tiene esa mascota")
                else:
                    break
            i["Mascotas"].append(id_mascota) # se agrega el id de la mascota a la informacion del veterinario
            j["Veterinario"]==id_veterinario
        
        print(f"\n  LISTA VETERINARIO\n{i}")
        print(f"\n  LISTA MASCOTAS\n{j}")
        
asignar()
            
    