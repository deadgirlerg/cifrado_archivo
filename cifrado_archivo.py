from cryptography.fernet import Fernet

def generar_clave():
    return Fernet.generate_key()

def cifrar_archivo(nombre_archivo, clave):
    fernet = Fernet(clave)
    with open(nombre_archivo, 'rb') as archivo_original:
        datos = archivo_original.read()
        datos_cifrados = fernet.encrypt(datos)
    with open(nombre_archivo + '.cifrado', 'wb') as archivo_cifrado:
        archivo_cifrado.write(datos_cifrados)
        print(f"Archivo '{nombre_archivo}' cifrado con éxito.")

def descifrar_archivo(nombre_archivo_cifrado, clave):
    fernet = Fernet(clave)
    with open(nombre_archivo_cifrado, 'rb') as archivo_cifrado:
        datos_cifrados = archivo_cifrado.read()
        datos_descifrados = fernet.decrypt(datos_cifrados)
    nombre_archivo_original = nombre_archivo_cifrado.rstrip('.cifrado')
    with open(nombre_archivo_original, 'wb') as archivo_original:
        archivo_original.write(datos_descifrados)
    print(f"Archivo '{nombre_archivo_cifrado}' descifrado con éxito.")

# Genera una clave (deberías almacenarla de manera segura)
clave = generar_clave()

# Nombre del archivo a cifrar
archivo_a_cifrar = 'archivo.txt'

# Cifrar el archivo
cifrar_archivo(archivo_a_cifrar, clave)

# Nombre del archivo cifrado
archivo_cifrado = 'archivo.txt.cifrado'

# Descifrar_archivo
descifrar_archivo(archivo_cifrado, clave)