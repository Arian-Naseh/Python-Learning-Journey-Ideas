city = "Amsterdam" #Create a variable city and store the name of your city
population = 5 #Create a variable population and store an integer value.

print ("the population of", city,"is", population) #Print both values in one sentence (e.g., “The population of Amsterdam is 145,000”).

a, b, c = 10, 20, 30  #Assign values 10, 20, 30 to three variables in a single line.
d = e = f = "python" #Assign the same string "Python" to three different variables.
#Print all variables.
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Take a number as input (string by default) from user
user_input = input("type your number")
#Convert it into int and float data types. Then store these values in two different variables.
user_input_int = int(user_input)
user_input_float = float(user_input)
# Print all three variables with their data types.
print(user_input, type(user_input))
print(user_input_int, type(user_input_int))
print(user_input_float, type(user_input_float))

#Create three variables for each data type: int, float, and complex.
age = 20 
height = 185.5
name = 5j
#Print the values of the variables and use the type() function to display their data types.
print(age, type(age))
print(height, type(height))
print(name, type(name))

