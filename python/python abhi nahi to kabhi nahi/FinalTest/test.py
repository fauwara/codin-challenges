"""
CodeForFreedom Challenge 20/04/2020

Write a program to print a list of strings in the predefined order, with the following modifications:
If the string’s length is equal to its printed position, convert string to UPPERCASE
	- Else convert the string to lowercase
	- Except if the string’s position is unchanged from its original position
	- Input will be a number N, then a list of N non-repeating numbers defining the required position of the string, and finally the list of N non-repeating strings. Output will be a list of N strings at the required location, with the required changes.

- Input:
5
5
4
3
1
2
Dog
Goat
Cat
Horse
Elephant

- Output:
horse
elephant
Cat
GOAT
dog
"""

listLength = int(input(''))
stringPositions = []
stringsList = [None] * listLength

for i in range(listLength):
	stringPositions.append(int(input('')))

for i in range(listLength):
	string = input('')
	if len(string) != stringPositions[i] or stringPositions[i] == i+1:
		stringsList[stringPositions[i]-1] = string.lower()
	else:
		stringsList[stringPositions[i]-1] = string.upper()

print(stringsList)
