import pandas as pd
import os
import csv


# Rutas de los archivos
archivo1 = "Lista negociada Febrero 2023.xlsx"
archivo2 = "Miscelaneos REF_TyP 2022 - Abril.xlsx"
archivo3 = "product.pricelist.csv"

def obtener_nombres_columnas(archivo, inicio=0):
    # Verificar si el archivo existe
    if not os.path.exists(archivo):
        print(f"El archivo '{archivo}' no existe.")
        return
    # Leer el archivo en un dataframe de pandas
    df = pd.read_excel(archivo, header=inicio)
    
    # # Imprimir los nombres de las columnas
    # print(f"Nombres de las columnas del archivo '{archivo}':")
    # print(df.columns.tolist())

# Llamar a la función para obtener los nombres de las columnas, comenzando en la línea 1
#obtener_nombres_columnas(archivo3, inicio=0)

def obtener_columnas_deseadas(archivo, id_columna_key, id_columna_val, ini):
    # Leer el archivo en un dataframe de pandas
    df = pd.read_excel(archivo)
    
    # Extraer las columnas deseadas
    columna_clave = df.iloc[ini:, id_columna_key]
    columna_valor = df.iloc[ini:, id_columna_val]
    
    # Construir el diccionario combinando las columnas
    diccionario_columnas = dict(zip(columna_clave, columna_valor))
    
    return diccionario_columnas

# Ruta del archivo
archivo1 = "Lista negociada Febrero 2023.xlsx"
# Índices de las columnas deseadas
id_column1_rf = 6  # Índice de la columna 6 (REFERENCIA INTERNA)
id_column2_price = 7  # Índice de la columna 7 (PRECIO MN)

# Obtener el diccionario de columnas
diccionario_columnas = obtener_columnas_deseadas(archivo1, id_column1_rf, id_column2_price, 2)


# print("Diccionario de columnas:")
# for key, value in diccionario_columnas.items():
#     print(f"{key}: {value}")


id_column1_rf = 9  # Índice de la columna 10 (PRECIO MN)
id_column2_price = 7  # Índice de la columna 8 (Codigo TyP)
#diccionario_columnas = diccionario_columnas + obtener_columnas_deseadas(archivo2, id_column1_rf, id_column2_price, 4)
diccionario_columnas.update(obtener_columnas_deseadas(archivo2, id_column1_rf, id_column2_price, 4))

# print("Diccionario de columnas:")
# for key, value in diccionario_columnas.items():
#     print(f"{key}: {value}")



# Función para leer el archivo CSV y cargarlo en una lista de diccionarios
def leer_csv(nombre_archivo):
    with open(nombre_archivo, newline='') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        return list(reader)

# Función para escribir en el archivo CSV con los cambios
def escribir_csv(nombre_archivo, datos):
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=datos[0].keys())
        writer.writeheader()
        writer.writerows(datos)

# Función para actualizar el archivo CSV usando el diccionario
def actualizar_csv(archivo_csv, diccionario):
    datos = leer_csv(archivo_csv)
    for fila in datos:
        valor_columna3 = fila['item_ids/product_id/default_code']
        if valor_columna3 in diccionario:
            fila['item_ids/fixed_price'] = diccionario[valor_columna3]
    escribir_csv("nuevos_precios_subir.csv", datos)  # Se guarda como "nuevos_precios_subir.csv"

# Ejemplo de uso
archivo_csv = archivo3  # Reemplazar con el nombre correcto del archivo
diccionario = diccionario_columnas  # Tu diccionario
actualizar_csv(archivo_csv, diccionario)
