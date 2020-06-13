# Pet = "Cat" * 3
# print(Pet)

# def double_word(word):
#     return word*2 + str(len(word * 2)) 

# print(double_word("hello")) # Should return hellohello10
# print(double_word("abc"))   # Should return abcabc6
# print(double_word(""))      # Should return 0

def first_and_last(message):
    if message == "":
        return True
    elif message[0] == message[-1]:
        return True
    else: 
        return False
        

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
