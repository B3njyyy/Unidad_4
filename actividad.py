import hashlib ## librería de Python que entrega funciones hash 
import sys ## permite leer documentos
import os ## permite verificar que el archivo existe

VERSION = "1.0.0" ## la primera versión del programa


## Función para calcular el hash
def sha256_file(archivo):
    
    sha = hashlib.sha256()
    with open(archivo, "rb") as f:
        sha.update(f.read())
    return sha.hexdigest()


def main():

    # si no se entregan argumentos al ejecutar
    if len(sys.argv) < 2:
        print("Uso: sha256-tool <archivo>")
        return

    archivo = sys.argv[1]

    # revisa si el archivo existe
    if not os.path.isfile(archivo):
        print("Archivo no encontrado")
        return

    # Calcular hash
    resultado = sha256_file(archivo)
    print("SHA-256:", resultado)

if __name__ == "__main__":
    main()
    input("\nPresiona Enter para salir...") # Se agrega esta linea para que el .exe no se cierre
