import csv

# if python is not installed, you can use py2exe (only on windows) to convert the python file to an exe file, if it is installed, run "python3 ./student.py" in a terminal while inside the folder containing "student.py"

final = []
# Change yog to be the correct OU
yog = '/Students/StudentsUnder13_restricted/ACES Students/YOG 2032.aces'

# make sure the student.csv is in the same folder as this file
# student.csv needs the following fields to work (the order they are in does not matter)
# FirstName
# LastName
# MiddleName
# LASID (Local Identifier)
with open('students.csv', 'r', encoding='utf-8-sig') as csv_file:
    file = csv.DictReader(csv_file, delimiter=',')
    for line in file:
        students = {}
        students['First Name [Required]'] = line['FirstName']
        students['Last Name [Required]'] = line['LastName']
        students['Password [Required]'] = "abcd" + line['LASID'].lstrip('0')
        students['Org Unit Path [Required]'] = yog
        if line['MiddleName'] == 'NMN':
            students['Email Address [Required]'] = line['FirstName'][0] + line['LastName'] + '@arrsd.org'
        else:
            students['Email Address [Required]'] = line['FirstName'][0] + line['MiddleName'][0] + line['LastName'] + '@arrsd.org'
        final.append(students)
    
keys = final[0].keys()

with open('emails.csv', 'w', newline='', encoding='utf-8-sig') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(final)
