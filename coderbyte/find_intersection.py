strArr = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]

def FindIntersection(strArr):

  # code goes here
  first = [int(num) for num in strArr[0].strip().replace(" ","").split(",")]
  second = [int(num) for num in strArr[1].strip().replace(" ","").split(",")]

  a, b = set(first), set(second)

  intersection = a.intersection(b)
  intersection_list = list(sorted(intersection))

  strArr = ""

  for num in intersection_list:
    if num == intersection_list[-1]:
      strArr += str(num)
    else:
      strArr += str(num) + ","

  return strArr

# keep this function call here
print(FindIntersection(input()))


# Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
# Output: 1,4,13
#
# Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
# Output: 1,9,10
