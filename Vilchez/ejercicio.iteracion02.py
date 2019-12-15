# Programa 02

import os
tipos_clientes=os.sys.argv[1]

for letra in tipos_clientes:
    if(letra=="A1"):
        print("Paga a tiempo")
    if(letra=="B2"):
        print("Demora en pagar dos dias")
    if(letra=="C3"):
        print("Demora en pagar un mes")
    if(letra=="D4"):
        print("No paga hasta que lo notifiquen")
#fin_for
