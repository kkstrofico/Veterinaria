import ClaseAdmin # Modulo aue contiene los metodos que puede ejecutar el administrador
import bsd # modulo que contiene las listas generales
print("\nINGRESA UNA OPCION\n")
def menu():
    while True:
        seleccion = input(f"\n\tINGRESAR COMO\n1. Administrador\n2. Veterinario:\n ")
        if seleccion != "1" and seleccion != "2":
            print("Error, ingresa una opcion correcta")
        else:
            break
    if seleccion =="1":
        print("""OPCIONES\n1. Registrar un veterinario\n2.  """)
        opcion_admin= input("Ingresa la opcion: ")
        if opcion_admin =="1":
            ClaseAdmin.admin.registrar_vet() # llamar el modulo ClaseAdmin que contiene la clase Admin y el metodo (registrar_vet) que  llama el modulo ClaseVeterinario que contiene la clase veterinario y se llama el metodo registrar_Veterinario
            print("Veterinario Registardo Exitosamente")  
            volver_menu()

def volver_menu(): # funcion que se encarga de posibilitar volver al menu
    while True:
        volver= input("Deseas volver al menu si/no: ").lower()
        if volver != "si" and volver != "no":
            print("Error, ingresa si/no")
        else:
            break
    if volver == "si":
        menu()
    else:
        print("Ok, hasta pronto")
        exit()
menu()
