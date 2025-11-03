

# ----------------------------------------
# Print Practice Exercises
# ----------------------------------------


# Print Practice #1
# Write Python code that prints the sentence: I love learning Python


print("I love learning Python")


# Print Practice #2
# Write Python code that prints the sentence: Learning with 'TOTAL Python' is super fun!
print("Learning with 'TOTAL Python' is super fun!")




# Print Practice #3
# Write Python code that prints the number 555 to the screen as a result of a mathematical expression
print(500 + 55)


##############################################################################################################
# Find 3 objects around the room and create variables from it,
# Insert those variables into an f-string sentence(look at slide 22)in repl.it
obj1="headphones"
obj2="hallpass"
obj3="clock"


sentence= f"our room has {obj1} ,  {obj2} and {obj3}"
print(sentence)


# Familiarize yourself with the syntax of the print() function.
# Print your name.
# Print today's date.
# Print the name of your favorite movie.
first_name = "Christian, gabe, alexis jonjon"
date= "October 30 2025"
favorite_movie = "GNFOS"




print(f"{first_name} the date is {date}  Fav movie {favorite_movie}")
# Print your name and age on separate lines using a single print() function.
# Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."
age=15
print(f"my name is {first_name} my age is {age}")
##############################################################################################################


###########################String Practice##################################
#syntax is the way we write code
print("Hello World")
name = "John"
#in other languages, this is different
# in javascript for example, you define
#variables with let or const or var
#in python, you just give your variables a
#name and then define it with a value




#challenge
# find a summary of the movie blue beetle online and create a 
# variable called blue_beetle_summary and print it it out to the screen






# print the length of the summary
# upper case the entire summary
# print the summary
# print the summary in lowercase
# replace the word blue with red
# print the summary
# string index the word beetle and print it out
# print the last word of the summary
# print the summary in reverse
blue_beetle_summary= "The film Blue Beetle (2023) follows Jaime Reyes, a recent college graduate who returns home to his family and discovers they are in financial trouble. His life changes forever when he accidentally bonds with an ancient alien scarab that grants him a powerful suit of armor with unpredictable abilities, transforming him into the superhero Blue Beetle. He must learn to control his powers to protect his family and stop Victoria Kord, the head of Kord Industries, who wants the scarab for her own military purposes." 


print(len(blue_beetle_summary))
print("Uppercase:", blue_beetle_summary.upper())
print("Lowercase:", blue_beetle_summary.lower())
red_beetle_summary= "The film Blue Beetle (2023) follows Jaime Reyes, a recent college graduate who returns home to his family and discovers they are in financial trouble. His life changes forever when he accidentally bonds with an ancient alien scarab that grants him a powerful suit of armor with unpredictable abilities, transforming him into the superhero Blue Beetle. He must learn to control his powers to protect his family and stop Victoria Kord, the head of Kord Industries, who wants the scarab for her own military purposes." 
print(len(red_beetle_summary))
print("Last character:", red_beetle_summary[-1])
reversed_string = red_beetle_summary[::-1]
print(red_beetle_summary)
##########################input practice#############################################
#input is when we ask the user for input/data
# Ask the user to enter their name.


# Input Practice #1
# Write Python code that allows the user to enter their answer, by making them the following question:
# What are you learning today?
# Your code must be able to print to the screen wh]
#whatever is entered by the user (use the print function).

q1= input("What are you learing today")
combined= ( q1 )
print("Your are learning " + combined)

# Input Practice #2
# Write Python code that allows the user to enter their answer, by making them the following question:
# Where are you from?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).

q1= input("Where are you from? ")
combined= ( q1 )
print("You're from " + combined)


# Input Practice #3
# Write Python code that displays the user's full name on the screen, by allowing them to enter their first and last name with the following instructions:
# What is your name?
# What is your surname?
# The code must be able to print the user's first and last name on the screen, separated by a space.


q1= input("What is your name? ")
q2= input("What is your Surrname?")
combined= ( q1  +  q2 )
print("Your name is  " +  combined)

# Exercise:
# Write a program that asks the user for their name and favorite color, then prints a message using both pieces of information.

q1= input("What is your name? ")
q2= input("What is your favorite color? ")
combined= ( q1 + "and "+ q2 )
print("Your answer were " + combined)



