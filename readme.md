# Script to create new students in bulk from pulled CSV on ASPEN

## Requires Python3 (https://www.python.org/downloads/)

### Make sure that python3 and pip are in your environmental variable paths

System Properties -> Environment Variables -> Path -> Edit -> add python3 and pip from installation folder

## To Use

Open python file in notepad or a different python editor and edit the "yog" variable to the desired OU
rename Aspen csv to students.csv
open command line, powershell, or a terminal
type "pip install csv"
type "python3 student.py" and press enter
within the folder you will find a new file called "emails.csv"
on google admin choose bulk upload and select the emails.csv file then upload
