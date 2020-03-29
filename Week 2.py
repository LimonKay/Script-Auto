# length = 10
# width = 2
# area = length*width
# print(area)

# # All ints are converted to floats

# base = 6
# height = 3 
# area = (base*height)/2
# print("The area of the trinagle is: " + str(area))


# def greeting(name, department):
#     print("Welcome, " + name)
#     print("You are part of " + department)

# # greeting("Key")
# # greeting("Camera")
# greeting("Blake", "IT Support")
# greeting("Ellis", "Soft engineering")


# def area_triangle(base, height):
#     return base*height/2

# area_a = area_triangle(5,4)
# area_b = area_triangle(7,3)
# sum = area_a + area_b
# print("The sum of both areas is: " + str(sum))

# def get_seconds(hours, minutes, seconds):
#   return 3600*hours + 60*minutes + seconds

# amount_a = get_seconds(2,30,0)
# amount_b = get_seconds(0,45,15)
# result = amount_a + amount_b
# print(result)

# // - floor division, divides and then turns into integer

# def print_monthly_expense(month, hours):
#     cost = hours*0.65
#     print("In " + month + " we spent: " + str(cost))


# print_monthly_expense("June",243)
# print_monthly_expense("July",325)
# print_monthly_expense("August",298)

# def rectangle_area(base, height):
# 	area = base*height  # the area is base*height
# 	print("The area is " + str(area))
	
# rectangle_area(5,6)

# # 1) Complete the function to return the result of the conversion
# def convert_distance(miles):
# 	return miles * 1.6  # approximately 1.6 km in 1 mile

# miles_driven = convert_distance(55)

# # 2) Convert my_trip_miles to kilometers by calling the function above
# my_trip_km = miles_driven

# # 3) Fill in the blank to print the result of the conversion
# print("The distance in kilometers is " + str(my_trip_km))

# # 4) Calculate the round-trip in kilometers by doubling the result,
# #    and fill in the blank to print the result
# print("The round-trip in kilometers is " + str(my_trip_km*2))



# # This function compares two numbers and returns them
# # in increasing order.
# def order_numbers(number1, number2):
# 	if number2 > number1:
# 		return number1, number2
# 	else:
# 		return number2, number1

# # 1) Fill in the blanks so the print statement displays the result
# #    of the function call
# smaller, bigger = order_numbers(100, 99)
# print(smaller, bigger)

# Let's revisit our lucky_number function. We want to change it, so that instead of printing the message, it returns the message. 
# This way, the calling line can print the message, or do something else with it if needed. Fill in the blanks to complete the code to make it work.


# def lucky_number(name):
#   number = len(name) * 9
#   message = "Hello " + name + ". Your lucky number is " + str(number)
#   return message
	    
# print(lucky_number("Kay"))
# print(lucky_number("Cameron"))

# You nailed it! In Python uppercase letters are alphabetically sorted before lowercase letters.

# If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. 
# A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. 
# Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?

# def calculate_storage(filesize):
#     block_size = 4096
#     # Use floor division to calculate how many blocks are fully occupied
#     full_blocks = 4096 // filesize
#     print(full_blocks)
#     # Use the modulo operator to check whether there's any remainder
#     partial_block_remainder = full_blocks % 2 == 0
#     # Depending on whether there's a remainder or not, return
#     # the total number of bytes required to allocate enough blocks
#     # to store your data.
#     if partial_block_remainder > 0:
#         return False
#     return True

# print(calculate_storage(1))    # Should be 4096
# print(calculate_storage(4096)) # Should be 4096
# print(calculate_storage(4097)) # Should be 8192
# print(calculate_storage(6000)) # Should be 8192

# def sum(x, y):
# 		return(x+y)
# print(sum(sum(1,2), sum(3,4)))

# print((10 >= 5*2) and (10 <= 5*2))


# The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1). ======================================
# Complete the body of the function so that it returns the right number. 
# Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.

# def fractional_part(numerator, denominator):
#     if denominator != 0:
#         return (numerator % denominator)/denominator

# print(fractional_part(5, 5)) # Should be 0
# print(fractional_part(5, 4)) # Should be 0.25
# print(fractional_part(5, 3)) # Should be 0.66...
# print(fractional_part(5, 2)) # Should be 0.5
# print(fractional_part(5, 0)) # Should be 0
# print(fractional_part(0, 5)) # Should be 0

# def format_name(first_name, last_name):
# 	# code goes here
# 	if first_name and last_name:
# 	  return "Name: " + last_name + ", " + first_name
# 	if first_name:
# 	  return "Name: " + first_name
# 	if last_name:
# 	  return "Name: " + last_name
# 	else: 
# 	  return
	  
# print(format_name("Ernest", "Hemingway"))
# # Should return the string "Name: Hemingway, Ernest"

# print(format_name("", "Madonna"))
# # Should return the string "Name: Madonna"

# print(format_name("Voltaire", ""))
# # Should return the string "Name: Voltaire"

# print(format_name("", ""))
# # Should return an empty string

# Complete the function by filling in the missing parts. The color_translator function receives the name of a color, then prints its hexadecimal value. 
# Currently, it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.

# def color_translator(color):
# 	if color == "red":
# 		hex_color = "#ff0000"
# 	elif color == "green":
# 		hex_color = "#00ff00"
# 	elif color == "blue":
# 		hex_color = "#0000ff"
# 	else:
# 		hex_color = "unknown"
# 	return hex_color

# print(color_translator("blue")) # Should be #0000ff
# print(color_translator("yellow")) # Should be unknown
# print(color_translator("red")) # Should be #ff0000
# print(color_translator("black")) # Should be unknown
# print(color_translator("green")) # Should be #00ff00
# print(color_translator("")) # Should be unknown

