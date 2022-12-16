from random import randint
import re

#Open the files

studentFile = open('students.txt', 'r')
emailFile = open('emails.txt', 'w')

#Read the student file line for their name

lines = studentFile.readlines()
for x in range (0, len(lines)):
    student = lines[x].split()

    #Add the student name with a random integar and '@poppleton.ac.uk' and then combine them
    
    email = student[2][0].lower()+'.' + student[1][:-1].lower() + str(randint(1111, 9999)) + '@poppleton.ac.uk'
    studentEmail = student[0] + " " + Email + "\n"

    #Write the email to the email file

    EmailFile.write(studentEmail)

# Closes the files
studentFile.close()
emailFile.close()
