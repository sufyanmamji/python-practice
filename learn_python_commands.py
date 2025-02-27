#Python Commands, their explanation and their examples.

#------------------------  TYPES OF VARIABLES  ------------------------#

#  There are 4 types of variables.
    
#Integers are whole numbers without a decimal
var_integer = 1

#Floats are numbers with decimal.
var_float = 1.2

#Strings are non numeric values.
var_strings = "String"

#Booleans are True / False vlues normally used for comparisons.
var_boolean = True

#------------------------  TYPES OF OPERATORS  ------------------------#

#Equality/inequality Operators are: == (equal), =< (less than equal to), => (greater than equal to), > (greater than), < (less than)
#Equality operators provide results in boolean form which helps in conditional application of code blocks. For Example:

print(var_integer == var_float)
#The answer is False because the vlues of these variables are not equal.

variable_1 = "value_1"
variable_2 = "value_2"

print(variable_1)
print(variable_2)

#A temporary variable can be introduced to swap values between variable_1 and variable_2. For Example:

temp_1 = variable_1
variable_1 = variable_2
variable_2 = temp_1

print(variable_1)
print(variable_2)

print(variable_2==temp_1)
#The answer is True

#We can get opposite boolean by using "NOT" command before boolean value or something resulting in a boolean value. For Example:

print(not variable_2==temp_1)
#The answer changed to False due to the use of "not" command.

#------------------------  IDENTIFY TYPES AND FORMAT  ------------------------#