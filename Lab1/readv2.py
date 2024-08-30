from scapy.all import rdpcap
import string

# Función para descifrar un mensaje cifrado con el cifrado César
def descifrar_cesar(texto, corrimiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            resultado += chr((ord(char) - corrimiento - offset) % 26 + offset)
        else:
            resultado += char
    return resultado

# Lista de palabras clave para identificar el mensaje correcto
palabras_clave = ["criptografia", "seguridad", "redes", "mensaje"]

# Función para identificar el mensaje más probable
def es_mensaje_probable(mensaje):
    for palabra in palabras_clave:
        if palabra in mensaje.lower():
            return True
    return False

# Función para imprimir mensajes y resaltar en verde el más probable
def probar_todos_corrimientos(texto):
    for corrimiento in range(26):
        mensaje_descifrado = descifrar_cesar(texto, corrimiento)
        if es_mensaje_probable(mensaje_descifrado):
            print(f"\033[92mDesp: {corrimiento}: {mensaje_descifrado}\033[0m")  # Imprime en verde
        else:
            print(f"Desp {corrimiento}: {mensaje_descifrado}")

# Leer los paquetes de un archivo .pcapng
def extraer_datos_pcapng(archivo_pcapng):
    paquetes = rdpcap(archivo_pcapng)
    datos = ""

    # Extraer datos ICMP
    for paquete in paquetes:
        if paquete.haslayer('ICMP') and hasattr(paquete['ICMP'], 'load'):
            datos += str(paquete['ICMP'].load.decode('utf-8', errors='ignore'))

    return datos

# Archivo .pcapng que contiene los paquetes capturados
archivo_pcapng = "cesar.pcapng"

# Extraer datos y ejecutar el ataque de fuerza bruta
datos_cifrados = extraer_datos_pcapng(archivo_pcapng)
if datos_cifrados:
    probar_todos_corrimientos(datos_cifrados)
else:
    print("No se encontraron datos ICMP en el archivo.")

