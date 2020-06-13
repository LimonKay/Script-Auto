# While Loops

# def attempts(n):
#     x = 1
#     while x <= n:
#         print("Attempt " + str(x))
#         x += 1
#     print("Done")
    
# attempts(2)

# /** NameError. This is the Python interpreter catching the mistake and telling you that you’re using an undefined variable.

# Infinite Loops

# def print_range(start, end):
# 	# Loop through the numbers from start to end
# 	n = start
# 	while n <= end:
# 		print(n)
# 		n = n + 1

# print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

# Fill in the blanks to make the print_prime_factors function print all the prime factors of a number. 
# A prime factor is a number that is prime and divides another without a remainder.






# The following code can lead to an infinite loop. Fix the code so that it can finish successfully for all numbers.
# Note: Try running your function with the number 0 as the input, and see what you get!


# Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. 
# A divisor is a number that divides into another without a remainder.

# def sum_divisors(n):
#   sum = 0
#   n % 1 == 
#   # Return the sum of all divisors of n, not including n
#   return sum

# # print(sum_divisors(0))
# # # 0
# print(sum_divisors(3)) # Should sum of 1
# # 1
# # print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# # # 55
# # print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# # # 114



# def attempts(n):
#     x = 1
#     while x <= n:
#         print("Attempt " + str(x))
#         x += 1
#     print("Done")
    
# attempts(2)

# def count_down(start_number):
#   current = 3
#   while (current > 0):
#     print(current)
#     current -= 1
#   print("Zero!")

# count_down(3)

# if x != 0:
#   while x % 2 == 0:
#   x = x / 2

# while x != 0 and x % 2 == 0:
#   x = x / 2 

# def print_range(start, end):
#   # Loop through the numbers from start to end
#   n = start
#   while n <= end:
#     print(n)
#     n = n + 1

# print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

# while True:
#   do_Something_cool()
#   if user_request_to_stop():
#     break

# def print_prime_factors(number):
#   # Start with two, which is the first prime
#   factor = 2
#   # Keep going until the factor is larger than the number
#   while factor <= number:
#     # Check if factor is a divisor of number
#     if number % factor == 0:
#       # If it is, print it and divide the original number
#       print(factor)
#       number = number / factor
#     else:
#       # If it's not, increment the factor by one
#       factor += 1
#   return "Done"

# print_prime_factors(100)
# # Should print 2,2,5,5
# # DO NOT DELETE THIS COMMENT

# def is_power_of_two(n):
#   # Check if the number can be divided by two without a remainder
#   while n % 2 == 0:
#     if n == 0:
#       return False
#     else:
#       return True
#   # If after dividing by two the number is 1, it's a power of two
#   if n == 1:
#     return True
#   return False
  

# print(is_power_of_two(0)) # Should be False
# print(is_power_of_two(1)) # Should be True
# print(is_power_of_two(8)) # Should be True
# print(is_power_of_two(9)) # Should be False

# The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5. 
# An additional requirement is that the result is not to exceed 25, which is done with the break statement. 
# Fill in the blanks to complete the function to satisfy these conditions.

# def multiplication_table(number):
# 	# Initialize the starting point of the multiplication table
# 	multiplier = 1
# 	# Only want to loop through 5
# 	while multiplier <= 5:
# 		result = number * multiplier 
# 		# What is the additional condition to exit out of the loop?
# 		if result > 25 :
# 			break
# 		print(str(number) + "x" + str(multiplier) + "=" + str(result))
# 		# Increment the variable for the loop
# 		multiplier += 1

# multiplication_table(3) 
# # Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

# multiplication_table(5) 
# # Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

# multiplication_table(8)	
# # Should print: 8x1=8 8x2=16 8x3=24

# Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. 
# A divisor is a number that divides into another without a remainder.

# def sum_divisors(n):
#   sum = 0
#   while n != n:
#     sum = n / n
#     return sum
#   # Return the sum of all divisors of n, not including n
  

# print(sum_divisors(0))
# # 0
# print(sum_divisors(3)) # Should sum of 1
# # 1
# print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# # 55
# print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# # 114


# # # # Want to try this out? Let's give it a go!
# # # # Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares of numbers between 0 and x (not included). 
# # # # Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (not included).

# # # def square(n):
# # #     return n*n

# # # def sum_squares(x):
# # #     sum = 0
# # #     for n in range(5):
# # #         sum += x+1
# # #     return n

# # # print(sum_squares(10)) # Should be 285

# def validate_users(users):
#   for user in [users]:
#     if len(user) >= 3:
#       print(user + " is valid")
#     else:
#       print(user + " is invalid")

# validate_users("purplecat")

# for x in range(1,11):
#   print(x**3)

# def retry(operation, attempts):
#   for n in range(attempts):
#     if operation():
#       print("Attempt " + str(n) + " succeeded")
#       break
#     else:
#       print("Attempt " + str(n) + " failed")

# retry(create_user, 3)
# retry(stop_service, 5)


# number = 1
# while number < 7:
# 	print(number, end=" ")
# 	number += 1

# def show_letters(word):
# 	for x in word:
# 		print(x)

# show_letters("Hello")
# # Should print one line per letter

# def counter(start, stop):
# 	x = start
# 	if start > stop:
# 		return_string = "Counting down: "
# 		while x >= stop:
# 			return_string += str(x)
# 			if x > stop:
# 				return_string += ","
# 			x-=1
# 	else:
# 		return_string = "Counting up: "
# 		while x <= stop:
# 			return_string += str(x)
# 			if x < stop:
# 				return_string += ","
# 			x+=1
# 	return return_string

# print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
# print(counter(2, 1)) # Should be "Counting down: 2,1"
# print(counter(5, 5)) # Should be "Counting up: 5"

# for x in range(10):
#     for y in range(x):
#         print(y)

# Want to try this out? Let's give it a go!

# Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares of numbers between 0 and x (not included). 
# Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (not included).

# def square(n):
#     return n*n

# def sum_squares(x):
#     sum = 0
#     for n in range(x):
#         sum += square(n)
#     return sum

# print(sum_squares(10)) # Should be 285

# def multiplication_table(start, stop):
# 	for x in range (start, stop+1):
# 		for y in range (start, stop+1):
# 			print(str(x*y), end=" ")
# 		print()

# multiplication_table(1, 3)

# Should print the multiplication table shown above

# def votes(yes, no, maybe):
# 	for vote in yes:
# 	    print("Possible option:" + vote)

# votes("yes", "no", "maybe")

# def loop(start, stop, step):
# 	return_string = ""
# 	if step == 0:
# 		step = 1
# 	if start > stop:
# 		step = abs(step) * -1
# 	else:
# 		step = abs(step)
# 	for count in range(start, stop, step):
# 		return_string += str(count) + " "
# 	return return_string.strip()

# print(loop(11,2,3)) # Should be 11 8 5
# print(loop(1,5,0)) # Should be 1 2 3 4
# print(loop(-1,-2,0)) # Should be -1
# print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24 
# print(loop(1,1,1)) # Should be empty

# def double_word(word):
#     return str(word*2) + str(len(word)*2)

# print(double_word("hello")) # Should return hellohello10
# print(double_word("abc"))   # Should return abcabc6
# print(double_word(""))      # Should return 0

def first_and_last(message):
    if message[0] == message[-1]:
      return True
    else:
      return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))