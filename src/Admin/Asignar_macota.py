import Veterinaria.src.bsd as bsd # se importa las listas que contienen todd la información
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
            while True:
                id_mascota= input("Ingresa el id de la mascota: ")
                if len(id_mascota) != 4:
                    print("El id de la mascota es de 4 digitos")
                elif id_mascota not in bsd.ides_mascotas:
                    print("Error, ese id no se encuentra")
                    # continuar JUNIOR
                
        
            
    
    