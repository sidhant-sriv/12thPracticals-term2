# Make a stack of dictionaries
stack = []
def insert_stack(stack, key, value):
    stack.append({key: value})

def remove_stack(stack):
    stack.pop()

def show_stack(stack):
    for i in stack:
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
        class_name = input("Enter the name of the class: ")
        Maths = int(input("Enter the number of Mathematics students: "))
        Physics = int(input("Enter the number of Physics students: "))
        Biology = int(input("Enter the number of Biology students:"))
        marks = {'Phy': Physics, 'Math': Maths, 'Bio': Biology}
        insert_stack(stack, class_name, marks)
    elif choice == "r":
        remove_stack(stack)
    elif choice == "s":
        show_stack(stack)
    elif choice == "e":
        print("bye")
        break
    else:
        print("Invalid choice")
