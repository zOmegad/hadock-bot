import csv
import glob
import os

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'z']
#juron_file = open('jurons.csv', 'w')

for letter in letters:
    with open('./src/' + letter + '_codification_alphanumérique_des_albums.csv') as csvfile:
        csv_reader = csv.reader(csvfile)
        writer = csv.writer(juron_file)
        for line in csv_reader:
            juron = line[0]
            writer.writerow([juron])
            print(juron)
