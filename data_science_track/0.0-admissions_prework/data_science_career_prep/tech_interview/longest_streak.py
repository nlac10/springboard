user_input = input("Please enter your exercise log: ")

def longest_streak(str):

    longest_streak = 0
    current_streak = 0

    ex_log = "-".join(str.lower().strip().replace(" ", "")).split("-")
    # print(ex_log)

    for log in ex_log:
        if log == 'y':
            current_streak += 1
            if current_streak > longest_streak:
                longest_streak = current_streak

        elif log == 'n':
            current_streak = 0

    return longest_streak

print(longest_streak(user_input))


# "Y N Ny y yy Y N NY  "
