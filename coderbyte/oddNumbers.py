l = int(input("Enter a number for l: "))
k = int(input("Enter a number for k: "))

def oddNumbers(l,k):
    # odds = []
    # numbers = [i for i in range(l,k+1)]
    # for num in numbers:
    #     if num % 2 == 0:
    #         continue
    #     else:
    #         odds.append(num)
    # return odds

    odds = [num for num in [i for i in range(l,k+1)] if num % 2 != 0]
    return odds

print(oddNumbers(l,k))
