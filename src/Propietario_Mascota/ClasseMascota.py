class Mascota: # clase mascota, que se encarga de recopilar la informacion de la mascota y subirla a la lista mascota
    def __init__(self, nombre, color, especie,raza,veterinario): # parametros que recibe la mascota
        self.nombre = nombre 
        self.color = color 
        self.especie = especie
        self.raza = raza
        self.veterinario = veterinario
        