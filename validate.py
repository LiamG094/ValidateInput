import time
fruit_list = [ "Apple", "Banana", "Orange", "Grapefruit", "Mango"] 

fruit = input("Select a fruit from the following list: " + str(fruit_list) )

if fruit in fruit_list:
    print("Enjoy your " + fruit)
else:
    print("Please select a fruit from the list!")