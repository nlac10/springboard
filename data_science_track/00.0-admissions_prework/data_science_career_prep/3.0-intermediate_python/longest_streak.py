# Longest Streak

"""
You want to track your longest consecutive streak exercising.
On a single line via std input, you're given the record over
several days.

Y means she exercised. N means no.

Y Y N Y Y Y N N Y

Streak is a set of consecutive Ys. Find the longest streak and
print out that number.

"""

# Y Y N Y Y Y N N Y
# my_rec = ['y','y','n','y','y','y','n','y']

exercise_rec = input("Please enter your exercise rec: Y/N ").lower().split()

def longest_streak(my_record):

    current_streak = 1

    for i in range(len(my_record)-1):

        if (my_record[i] == 'y') and (my_record[i+1] == 'y'):
            current_streak += 1
        elif (my_record[i] == 'n'):
            longest_streak = current_streak
            current_streak = 1

    if longest_streak > current_streak:
        return longest_streak
    else:
        return current_streak

        #
        # if my_record[i] == 'n':
        #     continue
        # elif (my_record[i] == 'y') and (my_record[i+1] == 'y'):
        #     streak += 1

    return streak



print(longest_streak(exercise_rec))
