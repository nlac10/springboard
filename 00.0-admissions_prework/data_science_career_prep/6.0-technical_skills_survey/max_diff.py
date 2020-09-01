"""
Title: Max difference
Source: Problem ques from sample technical test

Given a user inputted sequence of numbers on a single line separated by a space,
find the max difference between any two numbers in the list. Assume numbers can be positive, negative, or zero.
"""

# 1 9 2 -7 10 4 3

def max_diff(num_list):

    max_diff = 0

    for x in range(len(num_list)-1):
    # print(num_list[x])
        for y in range(1,len(num_list)):
            # print(num_list[y])
            # print(type(num_list[y]))

            # here you have to convert your numbers to ints because they are strings somehow

            diff = abs(int(num_list[x]) - int(num_list[y]))
            # print(max_diff)

            if diff > max_diff:
                max_diff = diff

    return max_diff


user_list = input("Please write a sequence of numbers: ").split(" ")

print(max_diff(user_list))

# this returns a string
# you need to convert it to a list
# num_list = user_list.split(" ")
# print(num_list)
# print(num_list)


# iterate through list first loop
# do second loop
# have container to hold abs((num1 - num2))
# compare first diff to next
