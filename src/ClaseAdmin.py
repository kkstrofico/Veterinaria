from itertools import chain # este modulo permite realizar la manipulacion de datos de manera rapida

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
                mascotas_asignadas=[] # lista donde se almacenaran las mascotas que se encuentran asignadas a un veterinario
                for k in bsd.lista_veterinarios:
                    mascotas_asignadas.append(k["Mascotas"])
                mascotas_asignadas_mod=list(chain.from_iterable(mascotas_asignadas)) # esto permite convertir varias listas en una sola

                for j in bsd.lista_mascota: # un for que iterara sobre las mascotas y mostrara las que no tienen veterinario
                    mascotas_sin_veterinario=[] # id de mascotas que no tienen veterinario
                    if j["Veterinario"]=="": # si en el diccionario de las mascotas, en la clave Veterinario tenga un valor, en caso    de que no, se le asignara el id del veterinario a essta mascota
                        mascotas_sin_veterinario.append(j["id"])
<<<<<<< HEAD
                        print(f"\n MASCOTAS SIN VETERINARIO\n {mascotas_sin_veterinario[0]}")
                        while True:
                            id_mascota= input("Ingresa el id de la mascota: ") # se solicita el numero de id de la mascota
                            if len(id_mascota) != 4:
                                print("El id de la mascota es de 4 digitos")
                            elif id_mascota not in bsd.ides_mascotas: # si el numero de ficha no se encuentra en la listaides_mascotas
                                print("Error, ese id no se encuentra")
                            elif id_mascota.isnumeric()==False:
                                print("Error, ingresa numeros")
                            elif id_mascota in i["Mascotas"]: # si el id de la mascota ya esta asignada al veterinario
                                print("Este veterinario ya tiene esa mascota")
                            elif id_mascota in mascotas_asignadas_mod:
                                print("Esa mascota ya le pertenece a otro veterinario")
                            else:
                                break
                        i["Mascotas"].append(id_mascota) # se agrega el id de la mascota a la informacion del veterinario
                        j["Veterinario"]=id_veterinario # se agrega el id del veterinario a la informacion de la mascota
                        print(f"\n  LISTA VETERINARIO\n{i}")
                        print(f"\n  LISTA MASCOTAS\n{j}")
                        while True:
                            agregar_mas= input("\nDesea agregar mascota a otro veterinario?\n ").lower().strip()
                            if agregar_mas != "si" and agregar_mas != "no":
                                print("Error, ingresa si/no")
                            else:
                                break
                        if agregar_mas =="si": # si dice que si 
                            if mascotas_sin_veterinario ==[]: # si la lista se encuentra vacia, significa que no hay mascotas por sin veterinario
                                print("No se encuentras mascotas sin veterinario")
                            else:  # de lo contrario se retorna de nuevo la funcion asignar
                                return admin.asignar()
                        else:
                            break # y si dice que no, finaliza el bucle



=======
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
                    elif id_mascota in mascotas_asignadas_mod:
                        print("Esa mascota ya le pertenece a otro veterinario")
                    else:
                        break
                i["Mascotas"].append(id_mascota) # se agrega el id de la mascota a la informacion del veterinario
                j["Veterinario"]==id_veterinario
            
            print(f"\n  LISTA VETERINARIO\n{i}")
            print(f"\n  LISTA MASCOTAS\n{j}")
    def registrar_veterinario(): #funcion que se encargara de pedir los datos del veterinario para ser almacenados
<<<<<<< HEAD
=======
=======
                j["Veterinario"]=id_veterinario # se agrega el id del veterinario a la informacion de la mascota
                print(f"\n  LISTA VETERINARIO\n{i}")
                print(f"\n  LISTA MASCOTAS\n{j}")
    
    
>>>>>>> e26b71d61c9a1a5504ff3e4fa7a9b259986c0a94
                #OPCION PARA CAMBIAR EL VETERINARIO DE UNA MASCOTA QUE YA TIENE VETERINARIO
                print("""\n DESEA MODIFICAR UN VETERINARIO DE LA MASCOTA QUE YA TIENE UN VETERINARIO ASIGNADO\n
                    1. SI / 2. NO""")
                while True:
                    seleccion = input("").lower() #solicitar si desea cambiar el veterinario de una mascota
                    if seleccion!= "si" and seleccion !="no":
                        print("error, ingresa si/no")
                    else:
                        break
                if seleccion =="si":
                    while True:
                        id_mascota_mod = input("Ingresa el id de la mascota: ") # solicitar el id de la mascota a la que se le modificara el veterinario
                        if len(id_mascota_mod) != 4:
                            print("Error, ingresa 4 digitos")
                        elif id_mascota not in bsd.ides_mascotas:
                            print("Error, ese id de mascota no se encuentra registrado")
                        else:
                            break
                    for m in bsd.lista_mascota: # recorrer la lista de las mascotas para cambiar su veterinario
                        if m["id"]== id_mascota_mod: # si el id es igual al que se encuentra en el diccionario
                            while True:
                                id_veterinario=input("Ingresa el id del veterinario que asignaras: ")
                                if id_veterinario not in bsd.ides_veterinarios:
                                    print("Error, ese id de veterinario no se encuentra registrado")
                                elif len(id_veterinario) != 10:
                                    print("Error, el ingresa 10 digitos")
                                else:
                                    break
                            # Asignar veterinario a mascota
                            m["Veterinario"]=id_veterinario
                    for v in bsd.lista_veterinarios: # Redcorrer la lista de los veterinarios para agregarle la mascota
                        if v["id"] ==id_veterinario: # si el id del diccionario es igual al id_veterinario ingresado
                            v["Mascotas"].append(id_mascota) # Agregar mascota a la lista mascotas del veterinario
                    print(bsd.lista_mascota)
                    print("")
                    print(bsd.lista_veterinarios)
                        
                        
                                    
                            
                        
                    
    def registrar_veterinario():
>>>>>>> 489d767e3eada7d92eea77dae86d4e409152bb4d
>>>>>>> 755b9147118fab9d82233b4ef46aa80a35b42e74
        while True: 
            try:
                id = str(input("Ingresa el id del veterinario: ")) #se pide el id 
                if id in bsd.ides_veterinarios or len(id) != 10: #se hace control de excepciones
                    print("\n\tALERT: el id ingresado ya se encuentra registrado, o el id debe tener 10 digitos")
                #if len(id) != 10:
                    #print("ERROR: el id debe tener 10 digitos")
                else:
                    while True:
                        nombre = str(input("ingresa el nombre del veterinario: ")) #pedir datos
                        if nombre.isnumeric() == True: #excepcion
                            print("\n\tERROR: el nombre no debe contener numeros")
                        else:
                            break
                    while True:
                        apellido = str(input("ingresa el apellido del veterinario: ")) #pedir datos
                        if apellido.isnumeric() == True: #excepcion 
                            print("\n\tERROR: el apellido no debe contener numeros")
                        else:
                            break
                    direccion = input("ingresa la direccion del veterinario: ")
                    break #sale del ciclo for
            except ValueError:
                print("\n\tERROR: el dato que ingresaste no es correcto")
        while True: #se crea un bucle
            try: 
                telefono = str(input("ingresa el telefono del veterinario: "))
                if len(telefono) != 10: #excepcion de 10 numeros
                    print("\n\tERROR: el telefono debe contener 10 digitos")
                else:
                    break
            except ValueError:
                print("\n\tERROR: dato ingresado no valido")
        tarjeta = ClasesVeterinario.Veterinario.tarjeta_profesional(None) #se llama a la funcion tarjeta profesional para agregar lo de la tarjeta profesional
        ClasesVeterinario.Veterinario(id,nombre,apellido,direccion,telefono,tarjeta) #se llama a la funcion clasesVeterinario para que se le asignen los datos que fueron ingresados
<<<<<<< HEAD
admin.asignar()
=======
    def consultar_mascotas_propietario():
        solic_id = str(input("ingresa el id del propietario: "))
        for i in bsd.lista_propietario:
            if str(i["id"]) == solic_id:
                print(f"Mascotas propietario: {i["mascotas"]}") #mostrar los datos del propietario
                mascota_selec=input("Ingresa el id de la mascota: ")
                #for y in bsd.ides_mascotas:
                if mascota_selec in bsd.ides_mascotas:
                    print(bsd.diccionario_mascota)
#admin.consultar_mascotas_propietario()

#admin.registrar_veterinario() #llamo la funcion
>>>>>>> e26b71d61c9a1a5504ff3e4fa7a9b259986c0a94
