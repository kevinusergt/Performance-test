def menu(): # menu display function
    print("\n---MAIN MENU---\n")
    print('1. Register student.')
    print('2. View students.')
    print('3. Search student.')
    print('4. Update student.')
    print('5. Delete student.')
    print('6. Exit.')
    
    
def register_students(students, name, id_user, age, course, state): #function to register students
    # create a dictionary 
    student ={
        'Name': name,
        'ID': id_user,
        'Age': age,
        'Course': course,
        'State': state
        }
    students.append(student) # add the dictionary into list
    print('Student has been added')
    
def Fetch(students): #function to display the list
    for s,student in enumerate(students,start=1):# list by index - element
        print(f"{s}. Name: {student['Name']} || ID: {student['ID']} || Age: {student['Age']} || Course: {student['Course']} || State: {student['State']}".strip())    

def consult(students, Id_search): # function to search for students
    for student in students: #loop to iterate
            if student['ID'] == Id_search:
                print('Student has been found')
                print(f"Name: {student['Name']} ID: {student['ID']} Age: {student['Age']} Course: {student['Course']} State: {student['State']}")
                break
    
def update_student(student, New_Name, New_ID, New_Age, New_Course, New_State): # function to update student information
        # assign the new values
        student['Name'] = New_Name
        student['ID'] = New_ID
        student['Age'] = New_Age
        student['Course'] = New_Course
        student['State'] = New_State
        print('Student has been updated')
        
def delete_student(students, ID_delete): # function to delete a student
    students.remove(ID_delete) #Remove a item of the list
    print('Student has been deleted')        