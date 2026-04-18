# ------------------------------------------


# HELPER FUNCTIONS 



# Add functions TODO
def add(num1, num2):
    return num1 + num2
# Subtraction function TODO
def sub(num1, num2):
    return num1 - num2 
# Division function TODO
def div(num1, num2):
    return num1 / num2
# Multiplication function TODO
def mult(num1, num2):
    return num1 * num2



# ------------------------------------------

# Ask for 2 numbers and operator TODO


# Write the logic for the calculator  TODO
# Use the functions 
num1 = int(input(" Give me 1 number: "))
num2 = int(input(" Give me another number: "))
operation = input(" Tell me what operation I have to do on these 2 numbers: ")

if operation == "add" :
    print(add(num1, num2))

elif operation == "sub" :
    print(sub(num1, num2))

elif operation  == "div" :
    print(div(num1, num2))

else : 
    print(mult(num1, num2))