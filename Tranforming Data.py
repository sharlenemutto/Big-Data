#This program gets student names and stores them in a list
def main():
    names = get_name()
    print('Names of the students enrolled:')
    print(names)
    print()
    
    #sort names list
    names.sort()
    print ('Sorted names: ', names)
    print()
    
    #reverse sort names list
    names.reverse()
    print('Reverse sorted names list:', names)
    print()
    
    #append instructor's name
    names.append('Professor Polanco')
    print(names)
    print()

    #insert my name into the list
    names.insert(0, 'Sharlene Mutto')
    print(names)

    #write names to an out file
    out_file = open('student.txt','w')
    for item in names:
        out_file.write(item +'\n')
    out_file.close()

    #read the student.txt file and print contents
    in_file = open('student.txt','r')
    line = in_file.read()
    print(line)
    #convert name list into a tuple and display
    names_tuple= tuple(names)
    print(names_tuple)
    
#function gets 12 students names and stores them in a list
#this returns the student list to the names variable above
def get_name():
    students = []
    for num in range (12):
        name = input('Enter student name: ')
        students.append(name)

    return students


    

main()
    
    
