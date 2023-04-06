import os

path = input("Ruta de la carpeta: \n")


def procesar_archivo(ruta):

    archivo_original = ruta

    nombre_archivo, extension = os.path.splitext(archivo_original)

    nueva_extension = ".EXE_"

    archivo_nuevo = nombre_archivo + nueva_extension

    os.rename(archivo_original, archivo_nuevo)


def recorrer_directorio(ruta):

    for nombre_archivo in os.listdir(ruta):
        ruta_archivo = os.path.join(ruta, nombre_archivo)

        if os.path.isdir(ruta_archivo):
            recorrer_directorio(ruta_archivo)

        else:
            procesar_archivo(ruta_archivo)

recorrer_directorio(path)
