# def first_and_last(message):
#     if message == "":
#         return True
#     elif message[0] == message[-1]:
#       return True
#     else:
#       return False

# print(first_and_last("else"))
# print(first_and_last("tree"))
# print(first_and_last(""))

# Strings in Python are immutable

# Want to try some string methods yourself? Give it a go!

# Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, in upper case. 
# For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.

# def initials(phrase):
#     words = phrase.split(" ")
#     result = ""
#     for word in words:
#         result += word[0]
#     return result.upper()

# print(initials("Universal Serial Bus")) # Should be: USB
# print(initials("local area network")) # Should be: LAN
# print(initials("Operating system")) # Should be: OS

# def student_grade(name, grade):
# 	return "{} received {}% on the exam".format(name, grade)

# print(student_grade("Reed", 80))
# print(student_grade("Paige", 92))
# print(student_grade("Jesse", 85))

# empty string is " "

# def double_word(word):
#     return str(word*2) + str(len(word)*2)

# print(double_word("hello")) # Should return hellohello10
# print(double_word("abc"))   # Should return abcabc6
# print(double_word(""))      # Should return 0

# def double_word(word):
#     return word*2 + str(len(word*2))

# print(double_word("hello")) # Should return hellohello10
# print(double_word("abc"))   # Should return abcabc6
# print(double_word(""))      # Should return 0

# def first_and_last(message):
#     if message == "":
#         return True
#     elif message[0] == message[-1]:
#       return True
#     else:
#       return False

# print(first_and_last("else"))
# print(first_and_last("tree"))
# print(first_and_last(""))

# def initials(phrase):
#     words = phrase.split(" ")
#     result = ""
#     for word in words:
#         result += word[0]
#     return result.upper()

# print(initials("Universal Serial Bus")) # Should be: USB
# print(initials("local area network")) # Should be: LAN
# print(initials("Operating system")) # Should be: OS

# def student_grade(name, grade):
# 	return "{} received {}% on the exam".format(name, grade)

# print(student_grade("Reed", 80))
# print(student_grade("Paige", 92))
# print(student_grade("Jesse", 85))


# def student_grade(name, grade):
# 	return "{name} received {grade}% on the exam".format(name=name, grade=grade)

# print(student_grade("Reed", 80))
# print(student_grade("Paige", 92))
# print(student_grade("Jesse", 85))


# The is_palindrome function checks if a string is a palindrome. 
# A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization.
# Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". 
# Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.

# Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase 
# "X miles equals Y km", with Y having only 1 decimal place. 
# For example, convert_distance(12) should return "12 miles equals 19.2 km".

# def convert_distance(miles):
# 	km = miles * 1.6 
# 	result = "{} miles equals {:.1f} km".format(miles,km)
# 	return result

# print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
# print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
# print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

# Weather = "Rainfall"
# print(Weather[:4])

# def nametag(first_name, last_name):
# 	return("{} {}.".format(first_name, last_name[0]))

# print(nametag("Jane", "Smith")) 
# # Should display "Jane S." 
# print(nametag("Francesco", "Rinaldi")) 
# # Should display "Francesco R." 
# print(nametag("Jean-Luc", "Grand-Pierre")) 
# # Should display "Jean-Luc G." 


# def is_palindrome(input_string):
# 	# We'll create two strings, to compare them
# 	new_string = ""
# 	reverse_string = ""
# 	# Traverse through each letter of the input string
# 	for word in input_string.upper():
# 		# Add any non-blank letters to the 
# 		# end of one string, and to the front
# 		# of the other string. 
# 		if word != ' ':
# 			new_string = new_string + word
# 			reverse_string = word + reverse_string
# 	# Compare the strings
# 	if new_string == reverse_string:
# 		return True
# 	return False

# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True

# def replace_ending(sentence, old, new):
# 	# Check if the old string is at the end of the sentence 
# 	if sentence.endswith(old):
# 		# Using i as the slicing index, combine the part
# 		# of the sentence up to the matched string at the 
# 		# end with the new string
# 		sentence = sentence.split(" ")
# 		sentence[-1]=new
# 		new_sentence = " ".join(sentence)
# 		return new_sentence

# 	# Return the original sentence if there is no match 
# 	return sentence
	
# print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# # Should display "It's raining cats and dogs"
# print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# # Should display "She sells seashells by the seashore"
# print(replace_ending("The weather is nice in May", "may", "april")) 
# # Should display "The weather is nice in May"
# print(replace_ending("The weather is nice in May", "May", "April")) 
# # Should display "The weather is nice in April"

# Using the "split" string method from the preceding lesson, complete the get_word function to return the {n}th word from a passed sentence. 
# For example, get_word("This is a lesson about lists", 4) should return "lesson", which is the 4th word in this sentence. 
# Hint: remember that list indexes start at 0, not 1.

# def get_word(sentence, n):
# 	# Only proceed if n is positive 
# 	if n > 0:
# 		words = sentence.split()
# 		# Only proceed if n is not more than the number of words 
# 		if n <= len(words):
# 			return(words[n-1])
# 	return("")

# print(get_word("This is a lesson about lists", 4)) # Should print: lesson
# print(get_word("This is a lesson about lists", -4)) # Nothing
# print(get_word("Now we are cooking!", 1)) # Should print: Now
# print(get_word("Now we are cooking!", 5)) # Nothing

# Let's use tuples to store information about a file: its name, its type and its size in bytes. 
# Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.

# def file_size(file_info):
# 	name, type, size= file_info
# 	return("{:.2f}".format(size / 1024))

# print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
# print(file_size(('Notes', 'txt', 496))) # Should print 0.48
# print(file_size(('Program', 'py', 1239))) # Should print 1.21

# Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to 
# return every other element from the list, ;/

# this time using the enumerate function to check if an element is on an even position or an odd position

# def skip_elements(elements):
#     result = []
#     for index,element in enumerate(elements):
#         if index % 2 == 0:
#             result.append(element)
#     return result

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

# def full_emails(people):
#     result = []
#     for email, name in people:
#         result.append("{} <{}>".format(name, email))
#     return result

# print(full_emails([("alex@example.com", "Alex Diego"),
# ("shay@example.com", "Shay Brandt")]))

# The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. 
# Fill in the blanks in the function, using list comprehension. 
# Hint: remember that list and range counters start at 0 and end at the limit minus 1.


# def odd_numbers(n):
# 	return [x for x in range(0,n+1) if x % 2 != 0]

# print(odd_numbers(5))  # Should print [1, 3, 5]
# print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
# print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
# print(odd_numbers(1))  # Should print [1]
# print(odd_numbers(-1)) # Should print []

# Given a list of filenames, we want to rename all the files with extension hpp to the extension h. 
# To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. 
# Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

# newfilenames = []  

# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate newfilenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.

# for filename in filenames:
#     if ".hpp" in filename:
#         newfilenames = [filename.replace('.hpp','.h') for filename in filenames]

# print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. 
# Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. 
# Or it can be written with a string using the letters r, w, and x or - when the permission is not granted. 
# For example: 640 is read/write for the owner, read for the group, 
# and no permissions for the others; converted to a string, it would be: "rw-r-----" 755 is read/write/execute for the owner, and read/execute for group and others; 
# converted to a string, it would be: "rwxr-xr-x" Fill in the blanks to make the code convert a permission in octal format into a string format.

# def octal_to_string(octal):
#     result = ""
#     value_letters = [(4,"r"),(2,"w"),(1,"x")]
#     for number in [int(n) for n in str(octal)]:
#         for value, letter in value_letters:
#             if number >= value:
#                 result += letter
#                 number -= value
#             else:
#                 result += "-"
#     return result
    
# print(octal_to_string(755)) # Should be rwxr-xr-x
# print(octal_to_string(644)) # Should be rw-r--r--
# print(octal_to_string(750)) # Should be rwxr-x---
# print(octal_to_string(600)) # Should be rw-------

# Let's create a function that turns text into pig latin: 
# a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.

# def pig_latin(text):
#   say = ""
#   # Separate the text into words
#   words = text.split()
#   for word in words:
#     # Create the pig latin word and add it to the list
#     words = word[1:] + word[:1] + "ay "
#     say += "".join(words)
#   return say
#     # Turn the list back into a phrase

# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"