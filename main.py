# import the functions files 
import src.functions

# create a empty list
students = []

# a loop reference
option = 0


while option < 6: 
    src.functions.menu() # import menu function
    try:# try the following 
        option = int(input('Choose an option: ')) # wait for an election
        if option == 0 or option < 0 or option > 6: #if the condition is True 
            option = 0 #restart the loop
            print('Type a valid option into menu.')
    
    except ValueError: #in case of letters and restart the loop
        print('Only number')
        
    
    
    if option == 1: #if the condition is True
        #create these variables
        Name =''#False
        Id_User = 0#False
        Age = 0#False
        Course ='' #False
        State = False#False
        
        while not Name: #deny the value
            Name = input('Type your name: ')
            if Name == ' ':
                print('Type a name')
                Name =''
                
        while not Id_User:#deny the value
            try: # try the following      
                Id_User = int(input('Type your ID: '))
                if Id_User < 0 or Id_User == 0:
                    print('Typer a valid ID')
                    Id_User = 0
                    continue
                elif any(Id_Valid['ID'] == Id_User for Id_Valid in students):
                    print('The ID already exists')
                    Id_User = 0
                    continue
            except ValueError:#except this problem
                print('Only number')
        
        while not Age:#deny the value
            try:# try the following 
                Age = int(input('Type your age: '))
                if Age < 0 or Age == 0 or Age >= 100:
                    print('Type a Valid age')
                    Age = 0
                    continue
            except ValueError:#except this problem
                print('Only number')
        
        while not Course:#deny the value
            Course = input('What is your Course: ')
            if Course == ' ':
                print('Please type a course')
                Course =''
        
        while not State:#deny the value
            State = input('Is the student activated? (S/N): ').upper() #wait for confirmation
            if State == 'S':
                State = 'Active'
                break 
            elif State == 'N':
                State = 'Inactive'
                break
            else:
                print('Type S or N')
                State = False # restart the loop
                            
        src.functions.register_students(students, Name, Id_User, Age, Course, State)                            
                            
    elif option == 2:
        if not students: # it denies value and works with false
            print('The list is empty')
        else:    
            src.functions.Fetch(students)    
    
    elif option == 3:
        if not students:# it denies value and works with false
                print('The list is empty')
        else:
            Id_search = 0 #reference
            while not Id_search:#deny the value
                
                try:
                    Id_search = int(input('Which is the ID: '))
                    if Id_search < 0 or Id_search == 0:
                        Id_search == 0
                        print('ID does not exist')
                    else:
                        src.functions.consult(students, Id_search)    
                except ValueError:#except this problem
                    print('Only number')
                 
    elif option == 4:
        if not students: #deny the value
            print('The list is empty')
        else:
            Id_search = 0
            while not Id_search:#deny the value
                
                try:# try the following 
                    Id_search = int(input('Which is the ID: '))
                    if Id_search < 0 or Id_search == 0:
                        Id_search == 0
                        print('ID does not exist')      
                    else:
                        for student in students: #loop that iterate the list
                            if student['ID'] == Id_search:
                                print('Student has been found ')
                                New_Name =''#False
                                New_Id_User = 0#False
                                New_Age = 0#False
                                New_Course ='' #False
                                New_State = False#False
                                
                                while not New_Name:#deny the value
                                    New_Name = input('Type a the new name: ')
                                    if New_Name == ' ' or New_Name == '':
                                        New_Name = student['Name']
                                    
                                while not New_Id_User:#deny the value
                                    try:# try the following 
                                        Replace = False
                                        while not Replace:#deny the value
                                            Replace = input('do you want to replace ID? (S/N): ').upper()#wait for confirmation
                                            if Replace == 'S':
                                                New_Id_User = int(input('Type a new ID: '))
                                                if New_Id_User == 0 or New_Id_User < 0:
                                                    New_Id_User = 0
                                                    print('ID is not valid')
                                                elif any(stud['ID'] == New_Id_User for stud in students):
                                                    New_Id_User = 0
                                                    print('ID already exist') 
                                            elif Replace == 'N':
                                                New_Id_User = student['ID']
                                            else:
                                                print('S or N')    
                                    except ValueError:#except this problem
                                        print('Only numbers')    
                                
                                while not New_Age:#deny the value
                                    try:# try the following 
                                        Replace_age = False
                                        while not Replace_age:#deny the value
                                            Replace_age = input('do you want to replace Age? (S/N): ').upper()#wait for confirmation
                                            if Replace_age == 'S':
                                                New_Age = int(input('Type a new Age: '))
                                                if New_Age == 0 or New_Age < 0:
                                                    New_Age = 0
                                                    print('Age is not valid')
                                            elif Replace_age == 'N':
                                                New_Age = student['Age']
                                            else:
                                                print('S or N')   
                                    
                                    except ValueError:#except this problem
                                        print('Only numbers') 
                                        
                                while not New_Course:#deny the value
                                    New_Course = input('Type the new course: ') 
                                    if New_Course == '' or New_Course == ' ':
                                        New_Course = student['Course']
                                while not New_State:
                                    New_State = input('Is the student activated? (S/N): ').upper()#wait for confirmation
                                    if New_State == 'S':
                                        New_State = 'Active'
                                        break 
                                    elif New_State == 'N':
                                        New_State = 'Inactive'
                                        break
                                    elif New_State == '' or New_State == ' ':
                                        New_State = student['State']
                                    else:
                                        print('Type S or N')
                                        New_State = False          
                                src.functions.update_student(student, New_Name, New_Id_User, New_Age, New_Course, New_State)
                                break
                            
                        else:
                            print('ID does not exist')        
                                
                          
                except ValueError:#except this problem
                    print('Only number')
    
    elif option == 5:
        if not students:
            print('The list is empty')
        else:    
            Id_delete= False
            while not Id_delete:#deny the value
                try:# try the following 
                    Id_delete = int(input('Type the ID: '))
                    if Id_delete < 0 or Id_delete == 0:
                        Id_delete = False
                        print('ID does not exist')
                    else:
                        for student in students:#loop that iterate the list
                            if student['ID'] == Id_delete:
                                print('ID has Found') 
                                delete = input('do you want to delete? (S/N): ').upper()#wait for confirmation
                                if delete == 'S':
                                    src.functions.delete_student(students,student) #call the functio to delete
                                    break
                                elif delete == 'N':
                                    break   #break the loop
                        else:
                            print(f'The ID {Id_delete} does not exist')
                except ValueError:#except this problem
                    print('Only number')
                        
            
    elif option == 6:
        print('Bye, Come back soon')  #Break the program                                         
