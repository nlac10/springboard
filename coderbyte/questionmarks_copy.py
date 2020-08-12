import string as s

def QuestionsMarks(str):

    # func accepts only single, digits (0-9), "?",
    # and alphabet (lower and upper)
    valid_input = s.ascii_letters + s.digits + "?"

    # if input string doesn't meet criteria, return false
    for char in str:
        if char not in valid_input:
            return "false"

    # container for number of "?"marks
    count = 0

    # iterate through inputted string and make into list
    string_list = []
    for char in str:
        string_list.append(char)

    # iterate through string_list and pull out only numbers
    num_list = []
    for item in string_list:
        if item.isdigit():
            num_list.append(item)

    # for numbers in number list, check if any two consecutive
    # numbers add to 10
    for idx in range(len(num_list)-2):
        if (int(num_list[idx]) + int(num_list[idx+1])) != 10:
            continue
        elif (int(num_list[idx]) + int(num_list[idx+1])) == 10:

            start_idx = string_list.index(num_list[idx])
            end_idx = string_list.index(num_list[idx+1])

            sliced_string = string_list[start_idx:end_idx]

            for char in sliced_string:
                if char == "?":
                    count += 1

    if count == 3:
        return ("true")
    else:
        return ("false")

"""
test cases
"""


# print(QuestionsMarks("acc?7??sss?1???rr9???1")) ## correct, returns true
# print(QuestionsMarks("acc?7??sss?2???rr9???1")) ## should be true, but returns false
print(QuestionsMarks("acc?7??sss?1???rr4???6")) #should be true, returns false
print(QuestionsMarks("acc?7??sss?1???rr4???6a")) #should be true, returns false
# print(QuestionsMarks("acc?7??sss?1???rr4????6")) # correct, returns false
