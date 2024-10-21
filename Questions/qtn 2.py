# Question 2(i)

# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese"
 

def calculate_bmi(weight,height):
     BMI = weight/height

     if weight <= 18.5:
            print("Underweight")
     elif 18.5 <= weight <=24.9:
            print("Normal weight")
     elif 25<=weight<=29.9:
            print("Overweight")
     else:
            print("obese")

     
     weight = float(input("\nEnter your weight here (kg):"))
     height = float(input("\nEnter your height here (m):"))

calculate_bmi(weight,height)

# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h. Choose a function name in line with what you want to 
# achieve. Radius r and height h should be in parameters. Make sure you use the real pie value (import math)

# def volume_of_cylinder():

#     radius = int(input("Enter the radius r: "))
#     height = int(input("Enter the height h: "))
#     import math
#     pie = math.pi
#     volume = pie*radius**2*height
#     print(f"The volume of the cylinder with radius {radius} and height {height} is {volume}")

# volume_of_cylinder()
