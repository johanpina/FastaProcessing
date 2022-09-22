import pandas as pd
import json

data = pd.read_excel('uniprotSalida.xlsx')

dataSample = []
print("Este es el tamaño de la Tabla ", data.shape)

for i in range(data.shape[0]):
    dataSample.append({
        "Entry":str(data['Entry'][i]),
        "Entry_Name":str(data['Entry Name'][i]),
        "Reviewed":str(data['Reviewed'][i]),
        "Organism":str(data['Organism'][i]),
        "Length":str(data['Length'][i]),
        "Secuence":str(data['Sequence'][i]),
        "EC_number":str(data['EC number'][i]),
        "PubMed_ID":str(data['PubMed ID'][i])
    })

jsonObject = json.dumps(dataSample,indent=4)

with open('dataProt.json', 'w') as outfile:
    outfile.write(jsonObject)