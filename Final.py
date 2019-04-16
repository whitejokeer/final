import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('generacion.csv')
delito = {'FEMINICIDIO':0,
          'ACTO SEXUAL VIOLENTO (CIRCUNSTANCIAS DE AGRAVACIÓN)':1,
          'ACCESO CARNAL O ACTO SEXUAL ABUSIVO CON INCAPAZ DE RESISTIR (CIRCUNSTANCIAS AGRAVACIÓN':2,
          'VIOLENCIA INTRAFAMILIAR':3,
          'ACCESO CARNAL ABUSIVO CON MENOR DE 14 AÑOS':4,
          'ACOSO SEXUAL':5,
          'HURTO RESIDENCIAS':6,
          'EXTORSIÓN':7,
          'ACTOS SEXUALES CON MENOR DE 14 AÑOS (CIRCUNSTANCIAS DE AGRAVACIÓN)':8,
          'ACCESO CARNAL VIOLENTO (CIRCUNSTANCIAS AGRAVACIÓN)':9,
          'HOMICIDIO CULPOSO ( EN ACCIDENTE DE TRÁNSITO)':10,
          'ACTO SEXUAL VIOLENTO' : 11,
          'HURTO PIRATERÍA TERRESTRE' : 12,
          'ESTÍMULO A LA PROSTITUCIÓN DE MENORES':13,
          'CONSTREÑIMIENTO A LA PROSTITUCIÓN':14,
          'HURTO ENTIDADES COMERCIALES':15,
          'INCAPACIDAD PARA TRABAJAR O ENFERMEDAD':16,
          'SECUESTRO EXTORSIVO':17,
          'SECUESTRO SIMPLE':18,
          'LESIONES CULPOSAS':19,
          'HURTO AUTOMOTORES':20,
          'ACCESO CARNAL ABUSIVO CON MENOR DE 14 AÑOS (CIRCUNSTANCIAS AGRAVACIÓN)':21,
          'PROXENETISMO CON MENOR DE EDAD':22,
          'DEMANDA DE EXPLOTACION SEXUAL COMERCIAL DE PERSONA MENOR DE 18 AÑOS DE EDAD':23,
          'HOMICIDIO':24,
          'HURTO MOTOCICLETAS':25,
          'ACCESO CARNAL O ACTO SEXUAL EN PERSONA PUESTA EN INCAPACIDAD DE RESISTIR  (AGRABADO)':26,
          'ACCESO CARNAL O ACTO SEXUAL ABUSIVO CON INCAPAZ DE RESISTIR':27,
          'PORNOGRAFÍA CON MENORES':28,
          'ACTOS SEXUALES CON MENOR DE 14 AÑOS':29,
          'HURTO ENTIDADES FINANCIERAS':30,
          'ACCESO CARNAL VIOLENTO':31,
          'LESIONES PERSONALES':32,
          'UTILIZACIÓN O FACILITACIÓN DE MEDIOS DE COMUNICACIÓN PARA OFRECER SERVICIOS SEXUALES DE MENORES':33,
          'ACCESO CARNAL O ACTO SEXUAL EN PERSONA PUESTA EN INCAPACIDAD DE RESISTIR':34,
          'INDUCCIÓN A LA PROSTITUCIÓN':35,
          'HURTO ABIGEATO':36,
          'LESIONES CULPOSAS ( EN ACCIDENTE DE TRANSITO )':37,
          'LESIONES AL FETO':38,
          'HURTO PERSONAS':39}

comuna= {
    '01. Norte':0,
    '02. Nor Oriental':1,
    '03. San Francisco':2,
    '04. Occidental':3,
    '05. García Rovira':4,
    '06. La Concordia':5,
    '07. La Ciudadela':6,
    '08. Sur Occidente':7,
    '09. La Pedregosa':8,
    '10. Provenza':9,
    '11. Sur':10,
    '12. Cabecera del Llano':11,
    '13. Oriental':12,
    '14. Morrorico':13,
    '15. Centro':14,
    '16. Lagos del Cacique':15,
    '17. Mutis':16
}
var = f"D{delito['LESIONES CULPOSAS']+1}C{comuna['06. La Concordia']+1}"
var2 = np.array(df[var],dtype=np.float64)

x=list(range(108))


fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')
ax1.plot(x,var2)

plt.show()


def quartiles(vec,n):
    q=0
    veccopy=vec
    veccopy=np.sort(veccopy)
    x=n*((len(veccopy)/4)+(1/2))
    for i in range(len(veccopy)):
        if(i<x and x<i+1):
            q=(veccopy[i]+veccopy[i+1])/2
    return  q
q1=quartiles(var2,1) # cambiar a por el vector que se quiere evaluar
q3=quartiles(var2,3)# cambiar a por el vector que se quiere evaluar
print(q1)
print(q3)
def atipicos(q1 ,q3,vec):
    ati=[]
    L1 = q3 + ((q3 - q1) * 1.5)
    L2 = q1 - ((q3 - q1) * 1.5)
    print(L1)
    print(L2)
    for i in range(len(vec)):
        if(vec[i]<L2 or vec[i]>L1):
            ati.append(i)
    return ati

atip = atipicos(q1,q3,var2)
print(atip)
def handler(atip_vec,vec ):
    val_atip=np.zeros(len(atip_vec))
    atipicos=np.asarray(atip_vec)
    for i in range(len(atipicos)):
        val_atip[i]=vec[atipicos[i]]
    return val_atip

val=handler(atip,var2)
x=np.asarray(range(0,len(var2)),dtype=np.float64)
def diferdiv_sqr(x,y,t):
    n=np.zeros((len(y),t+1),dtype=np.float64)
    for i in range(len(y)):
        n[i][0]=y[i]
    for k in range(1, t+1):
        for j in range (k,t+1):
            n[j][k]=(n[j][k-1]-n[j-1,k-1])-n[j-1,k-1]/(x[j]-x[j-k])
    return n
b=diferdiv_sqr(x,var2,len(x)-1)

def newton_m(n,b,x):# newton con matrix
    sum=0
    for i in range(len(x)):
            sum=b[i][i]*multiplicatoria(i,n,x)
    return sum
def multiplicatoria(limit,n,x):
    mul=1
    for i in range(limit):
        mul=mul*(n-x[i])
    return mul
for i in range(len(val)):
    res=newton_m(atip[i],b,x)
    print(res)


def li(limit , x , n):
    mul=1
    for j in range(len(x)):
        if(j != limit):
            mul=mul*(n-x[j])/(x[limit]-x[j])
    return mul
def lagrange(dato,x,n):
    sum=0
    for i in range(len(x)):
        sum+=li(i,x,n)*dato[i]
    return sum
print(lagrange(var2,x,atip[i]))



