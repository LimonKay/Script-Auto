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

