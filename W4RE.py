# Pet = "Cat" * 3
# print(Pet)

# def double_word(word):
#     return word*2 + str(len(word * 2)) 

# print(double_word("hello")) # Should return hellohello10
# print(double_word("abc"))   # Should return abcabc6
# print(double_word(""))      # Should return 0

# def first_and_last(message):
#     if message == "":
#         return True
#     elif message[0] == message[-1]:
#         return True
#     else: 
#         return False
        

# print(first_and_last("else"))
# print(first_and_last("tree"))
# print(first_and_last(""))


# def initials(phrase):
#     words = phrase.split()
#     result = ""
#     for word in words:
#         result += word[0]
#     return result.upper()

# print(initials("Universal Serial Bus")) # Should be: USB
# print(initials("local area network")) # Should be: LAN
# print(initials("Operating system")) # Should be: OS

# def student_grade(name, grade):
# 	return '{name} received {grade}% on the exam'.format(name=name, grade=grade)

# print(student_grade("Reed", 80))
# print(student_grade("Paige", 92))
# print(student_grade("Jesse", 85))


# toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
# toc["Epilogue"] = 39
# toc["Chapter 3"] = 24


# print(toc)
# if "Chapter 5" in toc:
#     print("True")
# else:
#     print("False")
# # ___ # Epilogue starts on page 39
# # ___ # Chapter 3 now starts on page 24
# # ___ # What are the current contents of the dictionary?
# # ___ # Is there a Chapter 5?

# cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
# for beast, limb in cool_beasts.items():
#     print("{} have {}".format(beast, limb))

# def skip_elements(elements):
# 	# Initialize variables
# 	new_list = []
# 	i = 0

# 	# Iterate through the list
# 	for x in elements:
# 		# Does this element belong in the resulting list?
# 		if x in elements:
# 			# Add this element to the resulting list
# 			new_list.append(x)
# 		# Increment i
# 		i += 1
# 	return new_list[::2]

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
# print(skip_elements([])) # Should be []

# def file_size(file_info):
# 	name, type, size= file_info
# 	return("{:.2f}".format(size / 1024))

# print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
# print(file_size(('Notes', 'txt', 496))) # Should print 0.48
# print(file_size(('Program', 'py', 1239))) # Should print 1.21def skip_elements(elements):

#     result = []
#     for index,element in enumerate(elements):
#         if index % 2 == 0:
#             result.append(element)
#     return result

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

