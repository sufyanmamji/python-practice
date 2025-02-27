##------------------------||  CONDITIONS & CODE BLOCKS  ||------------------------##

#The code under a condition with same indention is called a code block. It can a single line or multiple lines of code.
#A code block may contain further conditions and code blocks in it.

#Conditions are used to apply certain behavior of code. i.e.: if, elif, else. For Example:

variable_1 = 10
variable_2 = 20
variable_3 = 30

if True :
    print("Yes it's True")
#Due to the value "True" the print command will run. Similarly we can use a variable or comparison with a boolean output:

if (variable_1 + variable_2) == variable_3 :
    print("Because the comparison above is True")
#Due to True output value from the comparison the print command will run.

if False :
    print("Because the comparison above is not True")
#Due to the value "False" the print command will NOT run. Code Block will be skipped. Similarly we can use a variable or comparison with a boolean output:

if variable_1 == variable_3 :
    print("Because the comparison above is True")
#Due to False output value from the comparison the print command will NOT run. Code Block will be skipped.

#If we want to assign a behavior for a False output we use "else:" condition. For Example:

if variable_1 == variable_3 :
    print("The result of the comparison above is True")
else:
    print("The result of the comparison above is False")

#To apply multiple conditions in a code we use if, elif, else together. For Example:

x = 25

if variable_1 > x:
    print("The if condition will apply, because it is True.")
elif variable_2 > x:
    print("The first elif condition will apply.")
elif variable_3 > x:
    print("The second elif condition will apply.") 
else:
    print("Since all above conditions were false, this part will apply.")
print("This part is out of the code block so it runs anyway and not affected by the conditions.")
#The first True condition is applied.


#similar to Excel formulas we can use AND, OR operators to apply complex conditions. For Example:

x = 25
y = 50

if x < y and (y+x) == x:
    print("The if condition will apply, because it is True.")
elif (x+x) == y or (y+y) == x :
    print("The first elif condition will apply.")
else:
    print("Since all above conditions were false, this part will apply.")

