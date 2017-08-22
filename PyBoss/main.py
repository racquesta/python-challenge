import os
import csv

#choose 1 or 2
file_num = 2

#creates file path as file
file = os.path.join('raw_data', 'employee_data' + str(file_num) + '.csv')

#establishes lists for data
id_num = []
name = []
dob = []
ssn = []
full_state = []

# opens file, reads, and dumps to correct list
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)

    next(csvread, None)

    for row in csvread:
        id_num.append(row[0])
        name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        full_state.append(row[4])

first_name = []
last_name = []

#splits names and puts them in new, separate lists
for n in name:
    first_name.append(n.split(' ')[0])
    last_name.append(n.split(' ')[1])

month = []
day = []
year = []
#splits dob and puts them in new, separate lists for month, day, and yeat
for d in dob:
    year.append(d.split('-')[0])
    month.append(d.split('-')[1])
    day.append(d.split('-')[2])

format_dob = []
for m in range(len(month)):
    format_dob.append(month[m] + '/' + day[m] + '/' + year[m])

private_ssn = []
for num in ssn:
    private_ssn.append('***-**-' + num[-4:])

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

abbr_state =  []  
for state in full_state:
    abbr_state.append(us_state_abbrev[state])

clean_data = zip(id_num, first_name, last_name, format_dob, private_ssn, abbr_state)

output_file = os.path.join('Output', 'clean_emp_data' + str(file_num) + '.csv')

with open(output_file, 'w') as csvwrite:
    cleanfile = csv.writer(csvwrite, delimiter = ",")
    cleanfile.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    cleanfile.writerows(clean_data)
