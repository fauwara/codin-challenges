"""
Welcome. In this kata, you are asked to square every digit of a number.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
Note: The function accepts an integer and returns an integer
"""

def square_digits(num):
    numSeperatedList = []

    while num != 0:
        numSeperatedList.append(num%10) 
        num = int(num/10)

    reversedSquaredList = list(map(lambda x: x**2,numSeperatedList)) #.reverse()
    squaredList = reversedSquaredList[::-1]

    finalResult = 0

    for i in squaredList:
        numLength = len(str(i))
        finalResult = finalResult*(10**numLength) + i

    return finalResult

# TEST
print(square_digits(9119))