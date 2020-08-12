"""
What are the differences between del statement, .remove() and .pop()?
This is a great example of list comp and using range!
"""



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

array = [[numX,numY,numZ] for numX in range(x+1) for numY in range(y+1) for numZ in range(z+1)]
# print(array)

ans = sorted([array[x-1] for x in range(len(array)) if sum(array[x-1]) != n])

print(ans)




input: 
1
1
1
2

output:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
