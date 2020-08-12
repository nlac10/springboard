"""
brute force search
"""

def search(numbers, query_number):
    found_number = False

    for number in numbers:
        if number == query_number:
            found_number = True
            break

    return found_number


# Don't change code below this line
query_number = 45
numbers = [40, 512, 31, 3, 50, 610, 2]
print(search(numbers, query_number))

"""
binary
"""

def binary_search(list_of_numbers, query_item):
    #Set index of the first item in the list and an index of the last item in the list
    index_first = 0
    index_last = len(list_of_numbers)-1
    #Set the found variable to False
    found = False

    while (index_first <= index_last) and not found: #Check if the index_first is less than or equal to the index_last

        middle_index = (index_first + index_last)//2 #using index_first and index_last find the middle index

        if list_of_numbers[middle_index] == query_item: #Check if the middle element is equal to the query_item
            found = True
            break
        else:
            if query_item < list_of_numbers[middle_index]:
	            index_last = middle_index - 1#If the query_item is less than the middle item, use the index_last to eliminate the upper part of the list
            else:
                index_first = middle_index + 1

    #Return the found boolean variable
    return found

#Do not change code below this line
test_list = [4, 13, 22, 28, 34, 117, 943, 1032, 4222]
print(binary_search(test_list, 4222))
print(binary_search(test_list, 33))








"""
bubble
"""

def bubble_sort(list_of_numbers):
    for i in range(len(list_of_numbers)): #run N times, where N is number of elements in a list
        # Last i elements are already in place
        # It starts at 1 so we can access the previous element
        for j in range(1,len(list_of_numbers) - i): # N-i elements
            if list_of_numbers[j-1] > list_of_numbers[j] : #check if previous element is bigger than the current element
                #Swap code from the instructors notes:
                temp = list_of_numbers[j-1]
                list_of_numbers[j-1] = list_of_numbers[j]
                list_of_numbers[j] = temp

    return list_of_numbers

#Do not change code below this line
unsorted_list = [20, 31, 5, 1, 591, 1351, 693]
print(unsorted_list)
print(bubble_sort(unsorted_list))




"""
insert
"""

def insert_sort(list_of_numbers):

    for index in range(len(list_of_numbers)):

        current_element = list_of_numbers[index] #Access the current element
        position = index

        #Check if a position is greater than zero AND the previous item is greater than the current element
        while position > 0 and list_of_numbers[position - 1] > current_element:
            list_of_numbers[position] = list_of_numbers[position - 1] #Set the value of the positioned element to the value of the previous element. We are doing this to make space for the new (inserted item)
            position = position - 1 #Move position to one back

        #Set the value of the final positioned item to be the value of the current_element
        list_of_numbers[position] = current_element

    return list_of_numbers

#Do not change code below this line
list_of_numbers = [45,16,33,4,551,76,20]
print(list_of_numbers)
print(insert_sort(list_of_numbers))
