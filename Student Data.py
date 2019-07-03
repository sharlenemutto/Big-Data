#This program adds twelves student name and their average grades
#to grades.txt file

def main():
    #open and write student grades.txt file
    
    try:
        student_grade = open('grades.txt', 'w')
        
        #create a for loop
        for students in range(12):
            #Get student name
            name = input('Enter student name: ')
            ave_grade = float(input('Enter average grade: '))

            #Append the data to the file.
            student_grade.write(name +'\n')
            student_grade.write(str(ave_grade) +'\n')
                

        #close the file
        student_grade.close()
        
        print('Data appended to grades.txt')
    
    except ValueError as err:
        print('An error occured. Grade entered is out of range 1 and 100.')

    
    try:
        #open the grades.txt file
        grades = open('grades.txt','r')

        #read the first name field
        name = grades.readline()

        #read the rest of the file
        while name != '':
            #read the aveage grade field
            average = float(grades.readline())

            #strip the \n from student name
            name = name.rstrip('\n')

            #display the record.
            print('Name: ', name)
            print('Average Grade: ', average)

            #read the next student name
            name = grades.readline()
            
        #close the student grade file
        grades.close()
    
    except IOError:
        print('An error occured trying to read the file')
        print('Enter the correct file name.')
    except ImportError:
        print('An error occured trying to read the file')
        
#call the main function
main ()
