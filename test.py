import csv

with open("nbatotal.csv") as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')

	for row in readCSV:
		print(row)
