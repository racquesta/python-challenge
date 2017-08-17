import csv

data = []
with open('budget_data_1.csv') as cvsfile:
    readCSV = csv.reader(cvsfile, delimiter = ",")
    
    for row in readCSV:
        data.append(row)

total_months = len(data) - 1

for i in data:
    print(i[1])
    
print(total_months)


