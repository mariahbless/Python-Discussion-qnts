# Question 1(i)
# Temperature Classifier: Using a function, write a Python script that takes a temperature as input and classifies it into the 
# following categories: 
# Below 0°C: Freezing
# 0 to 10°C: Cold 
# 11 to 20°C; Moderate 
# 21 to 30°C: Warm 
# Above 30°C: Hot 

temperature = int(input('Enter the temperture here:'))
if 0 <temperature <=0:
    print(f" The temperature is Freezing ")
elif 0< temperature <=10:
    print(f"The temperature is cold")
elif 11< temperature <=20:
    print(f"The temperature is Moderate")
elif 21<temperature <=30:
    print(f"The temperature is Warm ")
elif temperature >= 30:
    print(f"The temperature is hot")
else:
    print(f" {temperature}  This temperature does not exist in the normal setting") 



# Question 1(ii)
# The volume of a sphere with radius r is (4/3)*pie*r**2. What is the volume of the sphere with radius 8. 
# Use a function and make sure the radius is entered from the keyboard and provide the answer in 1 decimal place
#ANSWER

#radius = int(input("Enter the radius here:"))
#Volume = (4/3)*(22/7)*radius**2
#print(f'The volume of the sphere is {Volume}')