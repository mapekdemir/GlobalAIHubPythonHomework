"""	@mapekdemir
The user will be defined. Get the data of this user by input method. Obtain information from user as follow: 
• First Name 
• Last name 
• Age 
• Date of birth (just year) 
Pass the user's information to the list and displays the screen using the for loop. Print all user information on the screen.
If he is under 18, print "You can't go out because it's too dangerous" on the screen. If he is over 18, print "You can go out to the street." on the screen. 
"""

list = []
firstName = input("Your First Name: ")
list.append(firstName)
lastName = input("Your Last Name: ")
list.append(lastName)
age = int(input("Your Age: "))
list.append(age)
birthYear = input("Your Year Birth: ")
list.append(birthYear)

print("User Information")
for l in list:
	print("- ", l)
	
if age < 0:
	print("Invalid login !")
elif age < 18:
	print("You can't go out because it's too dangerous.")
else:
	print("You can go out to the street.")