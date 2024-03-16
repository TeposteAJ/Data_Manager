import pandas as pd
import os


# Rutas de los archivos
archivo1 = "Lista negociada Febrero 2023.xlsx"
archivo2 = "Miscelaneos REF_TyP 2022 - Abril.xlsx"

def obtener_nombres_columnas(archivo, inicio=0):
    # Verificar si el archivo existe
    if not os.path.exists(archivo):
        print(f"El archivo '{archivo}' no existe.")
        return
    # Leer el archivo en un dataframe de pandas
    df = pd.read_excel(archivo, header=inicio)
    
    # Imprimir los nombres de las columnas
    print(f"Nombres de las columnas del archivo '{archivo}':")
    print(df.columns.tolist())

# Llamar a la función para obtener los nombres de las columnas, comenzando en la línea 1
#obtener_nombres_columnas(archivo1, inicio=2)
#obtener_nombres_columnas(archivo2, inicio=4)

    #df1 = pd.read_csv(archivo1)
    #df2 = pd.read_csv(archivo2)


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


print("Diccionario de columnas:")
for key, value in diccionario_columnas.items():
    print(f"{key}: {value}")


id_column1_rf = 9  # Índice de la columna 10 (PRECIO MN)
id_column2_price = 7  # Índice de la columna 8 (Codigo TyP)
diccionario_columnas = diccionario_columnas + obtener_columnas_deseadas(archivo2, id_column1_rf, id_column2_price, 4)
print("Diccionario de columnas:")
for key, value in diccionario_columnas.items():
    print(f"{key}: {value}")
