# My First Python Program
def print_table(table_of):

    for i in range(1, 11, 1):
        print(f"{table_of} x {i} = {table_of * i}")


print("until which table do you want to go: ")
num = int(input())

for x in range(1,num+1):
    print_table(x)

