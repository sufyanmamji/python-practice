#Python Commands, their explanation and their examples.

#------------------------||  TYPES OF VARIABLES  ||------------------------#

#  There are 4 types of variables.
    
#Integers are whole numbers without a decimal
var_integer = 1

#Floats are numbers with decimal.
var_float = 1.2

#Strings are non numeric values.
var_strings = "String"

#Booleans are True / False vlues normally used for comparisons.
var_boolean = True

#------------------------||  TYPES OF OPERATORS  ||------------------------#

#Equality/inequality Operators are: == (equal to), != (not equal to)f, =< (less than equal to), => (greater than equal to), > (greater than), < (less than)
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

#------------------------||  IDENTIFY & SWITCH DATA TYPES  ||------------------------#

#Value types in a variable can be identified using the command type() with variable name in the parenthesis. For Example:

print(type(var_integer))
print(type(var_float))
print(type(var_strings))
print(type(var_boolean))

#Type of Data can be switched using int(), str(), bool(), float(). For Example:

print(float(var_integer))
#a zero is added after decimal to convert a number into float.

print(int(var_float))
#Decimal and the values after that are removed to convert it into integer, no rounding off is done here.

print(str(var_float)== var_float)
#since string and float are not same the output is false.

print(bool(var_integer))
#zero and ones can be converted to boolean.

print(bool(0))
#zero and non-zero values can be converted to False for Zero and True for non-Zero values.

print(bool(var_strings))
#for all non-zero vlaues the output is True during conversion.

print(bool(str(0)))
#zero has to be an integer otherwise it will return True.

print(int(var_boolean))
#Similarly booleans can be converted to integers. i.e. 1 for True and 0 for Flase.


#------------------------XX  END  XX------------------------#