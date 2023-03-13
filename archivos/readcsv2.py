from Aprendiz import *
import csv
listaAprendices=[]
with open('C:\\Users\\usuario\\Documents\\01-SENA\\NetAcademy2023\\2693629.csv') as csvDataFile:

    csvReader=csv.reader(csvDataFile)    
    for row in csvReader:
        ob=Aprendiz(row[0],row[1],row[2],row[3])
        listaAprendices.append(ob)
        #print(row)
        # print('first name:',row[0])
        # print('last name:',row[1])
        # print('email:',row[2])
        # print('id:',row[3])

print(listaAprendices.nombreCompleto())
# for aprendiz in listaAprendices.sort():
#     print(aprendiz.nombreCompleto())
#print(listaAprendices[10])

