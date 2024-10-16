import bsd
import ClasesVeterinario
class admin:
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
    def registrarVeterinario():# Funcion que registra un veterinario
        while True:
            try:
                id = int(input("Ingresa el id del veterinario: "))
                if id in bsd.ides_veterinarios:
                    print("\n\tALERT: el id ingresado ya se encuentra registrado")
                else:
                    while True:
                        nombre = str(input("ingresa el nombre del veterinario: "))
                        if nombre.isnumeric() == True:
                            print("\n\tERROR: el nombre no debe contener numeros")
                        else:
                            break
                    while True:
                        apellido = str(input("ingresa el apellido del veterinario: "))
                        if apellido.isnumeric() == True:
                            print("\n\tERROR: el apellido no debe contener numeros")
                        else:
                            break
                    direccion = input("ingresa la direccion del veterinario")
                    break
            except ValueError:
                print("ERROR: el dato que ingresaste no es correcto")
        while True:
            try:
                telefono = int(input("ingresa el telefono del veterinario: "))
            except ValueError:
                print("\n\tERROR: dato ingresado no valido")
                break
        tarjeta = ClasesVeterinario.Veterinario.tarjeta_profesional()
        ClasesVeterinario.Veterinario(id,nombre,apellido,direccion,telefono,tarjeta)
admin.registrarVeterinario()