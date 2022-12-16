from random import randint
import re

studentFile = open('students.txt', 'r')
emailFile = open('emails.txt', 'w')
lines = studentFile.readlines()
for x in range (0, len(lines)):
    student = lines[x].split()
    email = student[2][0].lower()+'.' + student[1][:-1].lower() + str(randint(1111, 9999)) + '@poppleton.ac.uk'
    studentEmail = student[0] + " " + email + "\n"
    studentEmailClean = re.sub("['-]", "", studentEmail)
    emailFile.write(studentEmailClean)

studentFile.close()
emailFile.close()
