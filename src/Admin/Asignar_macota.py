from itertools import chain # este modulo permite realizar la manipulacion de datos de manera rapida

# Importamos el módulo 'sys' para acceder a las configuraciones del sistema
import sys  

# Añadimos la ruta de la carpeta que contiene el archivo 'bsd.py' a 'sys.path'.
# Esto le dice a Python que busque en esta carpeta cuando intentamos importar módulos.
sys.path.append((r'C:\Users\hp\OneDrive\Documentos\Veterinaria Repositorio\Veterinaria\src'))  

# Ahora, importamos el módulo 'bsd' desde la carpeta que acabamos de añadir a 'sys.path'.
# Python buscará 'bsd.py' en la ruta especificada y lo cargará.
import bsd  
