import csv
with open('C:\\Users\\usuario\\Documents\\01-SENA\\NetAcademy2023\\2693629.csv') as csvDataFile:
#with open('files/people.csv') as csvDataFile:
    csvReader=csv.reader(csvDataFile)
    #print(csvReader)
    for row in csvReader:
        #print(row)
        print('first name:',row[0])
        print('last name:',row[1])
        print('email:',row[2])
        print('id:',row[3])