import csv
import os

file = os.path.join('raw_data', 'budget_data_2.csv')

months = []
revenue = []

with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        revenue.append(int(row[1]))
        
total_months = len(months)

greatest_inc = revenue[1]-revenue[0]
greatest_dec = greatest_inc
total_revenue = revenue[0]

for r in range(1, len(revenue)):
    if revenue[r]-revenue[r-1] >= greatest_inc:
        greatest_inc = revenue[r]-revenue[r-1]
        great_inc_month = months[r]
    elif revenue[r]-revenue[r-1] <= greatest_dec:
        greatest_dec = revenue[r]-revenue[r-1]
        great_dec_month = months[r]
    total_revenue += revenue[r]

average_change = round((revenue[len(revenue)-1] - revenue[0])/(len(revenue)-1), 2)

print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(total_months))
print('Total Revenue: $' + str(total_revenue))
print('Average Revenue Change: $' + str(average_change))
print('Greatest Increase in Revenue: ' + great_inc_month + ' ($' + str(greatest_inc) + ')')
print('Greatest Decrease in Revenue: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')

output_dest = os.path.join('Output','pybank_output_2.txt')
        
with open(output_dest, 'w') as writefile:
    writefile.writelines('Financial Analysis' + '\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + great_dec_month + ' ($' + str(greatest_dec) + ')'+ '\n')



    
