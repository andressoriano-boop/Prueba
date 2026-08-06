from datetime import datetime, date

import requests
import zipfile
import io

import traceback

año = 2027
mes = datetime.now().month #mes actual

#Conocemos el trimestre actual
if mes in [1, 2, 3]:
    trimestre = 4
    NomMes = "Diciembre"
    mes = 12
elif mes in [4, 5, 6]:
    trimestre = 1
    NomMes = "Marzo"
    mes = 1
elif mes in [7, 8, 9]:
    trimestre = 2
    NomMes = "Junio"
    mes = 6
elif mes in [10, 11, 12]:
    trimestre = 3
    NomMes = "Septiembre"
    mes = 9

if trimestre == 4:
    año = año - 1 #Si es el trimestre 4, restar un año al año actual

url1 = "https://www.inegi.org.mx/contenidos/programas/ensu/datosabiertos/conjunto_de_datos_ensu_"
url2 = f"{str(año)}_{trimestre}t_csv.zip" #pegar año y trim actual
url = url1 + url2

respuesta = requests.get(url)

#Descargar y extraer el archivo zip
try:
    with zipfile.ZipFile(io.BytesIO(respuesta.content)) as archivo_zip:
        ruta1 = "conjunto_de_datos_ensu_cb_"
        if mes == 12:
            ruta2 = f"{str(mes)}{str(año)[-2:]}/conjunto_de_datos/conjunto_de_datos_ensu_cb_"
            ruta3 = f"{str(mes)}{str(año)[-2:]}.csv"
        else:
            ruta2 = f"0{str(mes)}{str(año)[-2:]}/conjunto_de_datos/conjunto_de_datos_ensu_cb_"
            ruta3 = f"0{str(mes)}{str(año)[-2:]}.csv"
        ruta = ruta1 + ruta2 + ruta3
        archivo_zip.extract(ruta, path=f"datos_ensu_{str(año)}_{trimestre}t")

except zipfile.BadZipFile:
    print("Error: El archivo descargado no es un archivo zip válido.")
    print(traceback.format_exc())
    raise
