# len(234) #len() does not take integer, it produces an error, TypeError
num_char = len(input("What is your name?"))
# print("Your name has" + num_char + "characters") #TypeError, can only concatenate str
print(type(num_char)) #type() to check the datatype of a variable

new_numChar = str(num_char) #type casting or type conversion

print("Your name has " + new_numChar + " characters")

print(70 + float(100.5))