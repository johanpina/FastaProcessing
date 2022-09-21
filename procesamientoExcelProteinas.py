from configparser import SectionProxy
import pandas as pd

data = pd.read_excel('uniprotSalida.xlsx')
print("El archivo cuenta con "+str(len(data['Entry']))+" secuencias de proteinas") ## Con esto puedo contar las proteinas que tiene el archivo.

revisados = data['Reviewed'] == 'reviewed' ## Con este voy a buscar en la columna "Reviewed" los que digan solo 'reviewed'

print(f"De las cuales {sum(revisados)} son proteinas revisadas (reviewed)") # imprimo la sumatoria de todos los valores positivos de la busqueda.

menoresa50 = data['Length'] <= 50 # Este es el filtro para saber el índice o numero de fila de las secuencias que son menores a 50


secuenciasmenores = data['Sequence'][menoresa50]

entrymenores = data['Entry Name'][menoresa50]
revisadosmenores = data['Reviewed'][menoresa50]
organismomenores = data['Organism'][menoresa50]
longitudmenores = data['Length'][menoresa50]

archivofasta = 'salida.fasta'

file = open(archivofasta,'w')

for entry,rev,org,long,secuen in zip(entrymenores,revisadosmenores,organismomenores,longitudmenores,secuenciasmenores):
    idSring = ">"+entry+" $ "+rev+" $ "+org+" $ "+str(long)+"\n" # Este es el Id que va a quedar en el FASTA
    file.write(idSring)
    file.write(secuen+"\n")

file.close()
print(f"Además , hay {sum(menoresa50)} secuencias <= 50 bases")



