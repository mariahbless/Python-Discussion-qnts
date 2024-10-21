#Question 3
# Using loop of your choice, WITI  has tasked you to automate a simple grading system. 
# As a python student, write a program using functions and conditions to display the grades that 
# the students will be receiving. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89% Grade is   B
# 70% - 79% Grade is   C                                                        
# 60% - 69%  Grade is  D                  
# 50% - 59%  Grade is  E  
# < 50%                Fail


def Grades():
    print("Calculate the grades of the candidates")


    marks = int(input('Enter the marks scored:\t'))
    if   90<=  marks <=100:
        print("Grade A")
    elif 80<=  marks <=89:
        print("Grade B") 
    elif  70<=  marks <=79:
        print("Grade C") 
    elif 60 <= marks <=69:
        print("Grade  D") 
    elif  50 <= marks <=59:
        print("Grade E")   
    else:
        print("Fail")  

Grades()