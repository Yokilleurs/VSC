import csv

#ouverture du fichier csv
def lecture_fichier(nom_fichier):
    with open(nom_fichier, mode='r') as fichier_ouvert:
        return list(csv.reader(fichier_ouvert,delimiter=","))


table = lecture_fichier('stations.csv')

len(table)

table[0]

table[21][1] = '43,2°'

for i in range(len(table)):
    table[i].append('')

