from Veterinario import ClasesVeterinario
import bsd

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
ClasesVeterinario.Veterinario(id,nombres,apellidos,direccion,telefono,tarjeta)
