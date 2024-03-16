import chardet

def detectar_codificacion(archivo):
    with open(archivo, 'rb') as f:
        resultado = chardet.detect(f.read())
    return resultado['encoding']

# Ejemplo de uso:
archivo = 'Lista negociada Febrero 2023.xlsx'
codificacion = detectar_codificacion(archivo)
print(f"La codificación del archivo {archivo} es: {codificacion}")
