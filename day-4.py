print("Welcome to the Interactive Personal Data Collector!")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
num = int(input("Please enter your favorite number: "))


print("Thank you! Here is the information we collected:")

print("Name: " ,name, "(Type: ",type(name), ",", "Memory Address: ", id(name), ")")
print("Age: ",age, "(Type: " ,type(age), "," , "Memory Address: ", id(age), ")")
print("Height: " ,height, "(Type: " ,type(height), "," , "Memory Address: ", id(height), ")")
print("Favourite Number: " ,num, "(Type: ", type(num), "," , "Memory Address: ", id(num), ")")

print("Your birth year is approximately: ")

print("Thank you for using the Personal data collector, GoodBye!!")