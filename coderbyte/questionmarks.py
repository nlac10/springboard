import string as s

def QuestionsMarks(str):

    accepted_input = s.ascii_letters + s.digits + "?"
    # return accepted_input

    for char in str:
        if char not in accepted_input:
            return "false"

    count = 0
    #
    # #
    string_list = []

    for char in str:
        string_list.append(char)

    # return(string_list)
    # outputs: ['a', 'c', 'c', '?', '7',
    # '?', '?', 's', 's', 's', '?', '3', 'r', 'r',
    # '1', '?', '?', '?', '?', '?', '?', '5']


    #
    num_list = []
    #
    for element in string_list:
        if element.isdigit():
            num_list.append(element)
    #
    # return(num_list)
    # outputs: [7, 3, 5, 5]

    # start_idx = None
    # end_idx = None

    # for x in range(len(num_list)-1):
    # # print(num_list[x])
    #     for y in range(1,len(num_list)):
    #         if (int(num_list[x]) + int(num_list[y])) != 10:
    #             continue
    #         elif (int(num_list[x]) + int(num_list[y])) == 10:
    #
    #             start_idx = string_list.index(num_list[x])
    #             end_idx = string_list.index(num_list[y])
    #
    #             # break
    #             print(start_idx,end_idx)
    #             # outputs: 4 11
    #
    #             sliced_string = string_list[start_idx:end_idx]
    #
    #             for char in sliced_string:
    #                 if char == "?":
    #                     count += 1


    for idx in range(len(num_list)-2):
        if (int(num_list[idx]) + int(num_list[idx+1])) != 10:
            continue
        elif (int(num_list[idx]) + int(num_list[idx+1])) == 10:

            start_idx = string_list.index(num_list[idx])
            end_idx = string_list.index(num_list[idx+1])
            # print(start_idx,end_idx)
            # outputs: 4 11

            sliced_string = string_list[start_idx:end_idx]

            for char in sliced_string:
                if char == "?":
                    count += 1

    # return(sliced_string)
    # print(sliced_string)
    # output: ['7', '?', '?', 's', 's', 's', '?', '3']
    # for char in sliced_string:
    #     if char == "?":
    #         count += 1


    if count == 3:
        return ("true")
    else:
        return ("false")

# print(QuestionsMarks("acc?7??sss?1???rr9???1")) ## correct, returns true
# print(QuestionsMarks("acc?7??sss?2???rr9???1")) ## should be true, but returns false
print(QuestionsMarks("acc?7??sss?1???rr4???6")) #should be true, returns false
print(QuestionsMarks("acc?7??sss?1???rr4???6a")) #should be true, returns false
# print(QuestionsMarks("acc?7??sss?1???rr4????6")) # correct, returns false

# keep this function call here
# print(QuestionsMarks(""))
#
# def QuestionsMarks(str):
#   last_number = None
#   nr_of_questions = 0
#
#   for l in str:
#
#     if l.isdigit():
#       if last_number is not None and (last_number + int(l)) == 10 and nr_of_questions == 3:
#         return "true"
#       else:
#         last_number = int(l)
#
#       nr_of_questions = 0
#
#     if l == '?':
#       nr_of_questions += 1
#
#   return "false"
#
# keep this function call here
# QuestionsMarks("acc?7??sss?3??rr4????6")
