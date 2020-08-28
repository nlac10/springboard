#All function that you have implemented in the previous steps
def push(stack, new_item):
	stack.append(new_item)

def is_empty(stack):
	return stack == []

def size(stack):
    return len(stack)

#Do not change any code above this line.

def reverse_string(string):
    #We have defined the stack for you
    stack = []

    for char in string:
        push(stack, char) #push to stack

    new_string = ""

    while not is_empty(stack): #Check if the stack is empty
        new_string += "" + stack.pop() #pop the last element

    return new_string


#Tests
#Do not change code below this line
assert reverse_string("programming") == "gnimmargorp"
print("Awesome job!")
print(reverse_string("programming"))
