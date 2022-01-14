# Employee management system using a stack of dictionaries

stack = []

def AddEmployee(stack):
    name = input("Enter employee name: ")
    salary = int(input("Enter employee salary: "))
    stack.append({'name': name, 'salary': salary})
def RemoveEmployee(stack):
    stack.pop()
def ShowEmployee(stack):
    if len(stack) == 0:
        print("No employees")
    else:
        s = sorted(stack, key=lambda x: x['name'])
        for i in s:
           for k, v in i.items():
               print("{} = {}".format(k, v))
# Command line menu
while True:
    print("""
    1. Insert
    2. Remove
    3. Show
    4. Exit
    """)
    choice = input("Would you like to insert, pop from stack, show the stack or exit? (i,r,s,e): ")
    if choice == "i":
        AddEmployee(stack)
    elif choice == "r":
        RemoveEmployee(stack)
    elif choice == "s":
        ShowEmployee(stack)
    elif choice == "e":
        print("bye")
        break
    else:
        print("Invalid choice")
