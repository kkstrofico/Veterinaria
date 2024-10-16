from Veterinario import ClasesVeterinario #se importa el modulo claseVeterinario que contiene todos los datos del veterinario
import bsd #importamos modulo que contiene las listas y diccionarios donde se almacenaran los datos

while True: 
    try:
        id = int(input("Ingresa el id del veterinario: ")) #se pide el id 
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
            direccion = input("ingresa la direccion del veterinario")
            break #sale del ciclo for
    except ValueError:
        print("ERROR: el dato que ingresaste no es correcto")
while True: #se crea un ciclo for 
    try:
        telefono = int(input("ingresa el telefono del veterinario: "))
        if len(telefono) != 10: #excepcion de 10 numeros
            print("ERROR: el telefono debe contener 10 digitos")
    except ValueError:
        print("\n\tERROR: dato ingresado no valido")
    break
tarjeta = ClasesVeterinario.Veterinario.tarjeta_profesional() #se llama a la funcion tarjeta profesional para agregar lo de la tarjeta profesional
ClasesVeterinario.Veterinario(id,nombre,apellido,direccion,telefono,tarjeta) #se llama a la funcion clasesVeterinario para que se le asignen los datos que fueron ingresados
