import json
import os
import modulos.menus as menus

def guardarArchivo(Diccionario,archivo):
    with open (f"./datos/administradorDataBase.json","w") as salida:
        json.dump(Diccionario, salida)
        return True
    
def abrirArchivo(archivo):
    arcPath = f"./datos/administradorDataBase.json"

    if not os.path.exists(arcPath):
        print(f"El archivo {arcPath} no existe.")
        return None
    
    with open(arcPath, "r") as entrada:
        nuevoDiccionario = json.load(entrada)
        return nuevoDiccionario
    
administradorInfo = abrirArchivo("administradorDataBase")

def ingresarAdministrador(administradorInfo: dict):
    idIngresado = input("Ingrese su documento:) ")
    if idIngresado in administradorInfo:
        administradorLogueado = administradorInfo[idIngresado]
        nombre = administradorInfo[idIngresado]["nombre"]
        print(f"Bienvenido {nombre}")
        return administradorLogueado
    else:
        print("ID no registrado")