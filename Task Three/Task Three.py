from random import randint 

#Open the files

StudentFile = open('students.txt', 'r')
EmailFile = open('emails.txt', 'w')

#Read the student file line for their name

lines = StudentFile.readlines()
for x in range (0, len(lines)):
    Student = lines[x].split()

    #Add the student name with a random integar and '@poppleton.ac.uk' and then combine them

    Email = Student[2][0].lower()+'.' + Student[1][:-1].lower() + str(randint(1111, 9999)) + '@poppleton.ac.uk'
    StudentEmail = Student[0] + " " + Email + "\n"

    #Write the email to the email file

    EmailFile.write(StudentEmail)

    # Closes the files
    StudentFile.close()
    EmailFile.close()
