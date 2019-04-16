import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import the dataset y filtramos
dataset = pd.read_csv('Delitos_en_Bucaramanga_2010_-_2018.csv')

dts_filtrada = dataset.iloc[:,[1,2,6,7,8,13,14,15,18]]
dts_filtrada = dts_filtrada.rename(columns = {'CLASIFICACIONES DELITO' : 'CLASIFICACION_DELITO'})

delitos = set(dts_filtrada.iloc[:,5])
meses = ['01. enero','02. febrero','03. marzo','04. abril','05. mayo','06. junio','07. julio','08. agosto','09. septiembre','10. octubre','11. noviembre','12. diciembre']
comuna= ['01. Norte','02. Nor Oriental','03. San Francisco','04. Occidental','05. García Rovira','06. La Concordia','07. La Ciudadela','08. Sur Occidente','09. La Pedregosa','10. Provenza','11. Sur','12. Cabecera del Llano','13. Oriental','14. Morrorico','15. Centro','16. Lagos del Cacique','17. Mutis']
años = [2010,2011,2012,2013,2014,2015,2016,2017,2018]

def filtradoDatos():
    info = np.zeros((108, 680))
    x = 0
    y = 0
    # Cantidad delito = 40

    # Orden delitos: 'FEMINICIDIO', 'ACTO SEXUAL VIOLENTO (CIRCUNSTANCIAS DE AGRAVACIÓN)',
    # 'ACCESO CARNAL O ACTO SEXUAL ABUSIVO CON INCAPAZ DE RESISTIR (CIRCUNSTANCIAS AGRAVACIÓN','VIOLENCIA INTRAFAMILIAR', 'SECUESTRO EXTORSIVO', 'LESIONES CULPOSAS ( EN ACCIDENTE DE TRANSITO )',
    # 'HURTO ENTIDADES FINANCIERAS', 'HURTO PERSONAS', 'HURTO AUTOMOTORES', 'INCAPACIDAD PARA TRABAJAR O ENFERMEDAD',
    # 'ACTOS SEXUALES CON MENOR DE 14 AÑOS (CIRCUNSTANCIAS DE AGRAVACIÓN)', 'EXTORSIÓN', 'HOMICIDIO CULPOSO ( EN ACCIDENTE DE TRÁNSITO)',
    # 'ACCESO CARNAL O ACTO SEXUAL ABUSIVO CON INCAPAZ DE RESISTIR', 'ACOSO SEXUAL',
    # 'ACCESO CARNAL VIOLENTO (CIRCUNSTANCIAS AGRAVACIÓN)', 'ACCESO CARNAL VIOLENTO', 'LESIONES CULPOSAS', 'HURTO RESIDENCIAS',
    # 'SECUESTRO SIMPLE', 'PROXENETISMO CON MENOR DE EDAD', 'CONSTREÑIMIENTO A LA PROSTITUCIÓN', 'HURTO MOTOCICLETAS', 'FEMINICIDIO',
    # 'ACCESO CARNAL O ACTO SEXUAL EN PERSONA PUESTA EN INCAPACIDAD DE RESISTIR',
    # 'ACCESO CARNAL O ACTO SEXUAL EN PERSONA PUESTA EN INCAPACIDAD DE RESISTIR  (CIRCUNSTANC',
    # 'HOMICIDIO', 'ACCESO CARNAL ABUSIVO CON MENOR DE 14 AÑOS', 'LESIONES PERSONALES', 'HURTO ENTIDADES COMERCIALES',
    # 'PORNOGRAFÍA CON MENORES', 'ACCESO CARNAL ABUSIVO CON MENOR DE 14 AÑOS (CIRCUNSTANCIAS AGRAVACIÓN)',
    # 'ACTO SEXUAL VIOLENTO (CIRCUNSTANCIAS DE AGRAVACIÓN)', 'HURTO PIRATERÍA TERRESTRE',
    # 'ACCESO CARNAL O ACTO SEXUAL ABUSIVO CON INCAPAZ DE RESISTIR (CIRCUNSTANCIAS AGRAVACIÓN',
    # 'LESIONES AL FETO', 'HURTO ABIGEATO', 'INDUCCIÓN A LA PROSTITUCIÓN', 'ESTÍMULO A LA PROSTITUCIÓN DE MENORES',
    # 'UTILIZACIÓN O FACILITACIÓN DE MEDIOS DE COMUNICACIÓN PARA OFRECER SERVICIOS SEXUALES DE MENORES',
    # 'ACTO SEXUAL VIOLENTO', 'DEMANDA DE EXPLOTACION SEXUAL COMERCIAL DE PERSONA MENOR DE 18 AÑOS DE EDAD',
    # 'ACTOS SEXUALES CON MENOR DE 14 AÑOS'
    for i in delitos:
        dts_delito = dts_filtrada[dts_filtrada.CONDUCTA == i]
        # Cantidad comunas de Bucaramanga = 17
        for j in comuna:
            dts_delitos_comuna = dts_delito[dts_delito.NOM_COMUNA == j]
            for z in años:
                for k in meses:
                    if (x == 108):
                        x = 0
                    if (y == 680):
                        y = 0
                    info[x][y] = (
                        len(dts_delitos_comuna[(dts_delitos_comuna.AÑO == z) & (dts_delitos_comuna.MES == k)]))
                    x = x + 1
            y = y + 1
    return info


info = filtradoDatos()
def generacionNombres():
    nombreColumna = []
    contador = 0
    for i in range(40):
        for j in range(17):
            dato = "D"+str(i+1)
            dato = dato +"C"+str(j+1)
            nombreColumna.append(dato)
            dato = ""
    return nombreColumna
nombreColumna = generacionNombres()
generacionNombres()
def generacionDataFiltrada(info):
    my_df = pd.DataFrame(info)
    my_df.to_csv('generacion.csv', header=nombreColumna)
generacionDataFiltrada(info)
df = pd.read_csv('generacion.csv')
print(np.array(df["D1C2"]))