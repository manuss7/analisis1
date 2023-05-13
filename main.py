import pandas as pd

#organizar datos

tabla1=pd.read_csv("./data/empleados.csv")

from data.comidas import comidas

tabla2 =pd.DataFrame(comidas)
from data.medicos import crearMedicos
medicos=crearMedicos()

tabla3=pd.DataFrame(medicos)

tabla1Modificada=tabla1.head()
print (tabla1Modificada)(50)
