"""
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.
"""

s = 'abcbbbbbabcdefghjklmnabbdefghjklmn'


begOfString = 0
endOfString = 1
bestString = ''

for i in range (len(s)):
	currentString = s[begOfString:endOfString]
	alphString = ''.join(sorted(currentString)) #make an alphabetical version of currentString.

	if currentString == alphString: #check if currentString is identical to the alphabetically ordered one.

		if (len(currentString)) > (len(bestString)): #swaps out the prevously  best string  if currentString is longer.
			bestString = currentString
			endOfString += 1 #adds one more letter to be tested.

		elif currentString == bestString:
			endOfString += 1

		else:
			endOfString += 1 #if currentString is in alphabetical order but not longer than best string, it moves on to the next letter here.
			
	else:
		begOfString += 1 # += len(currentString) -1, might make it more efficient, but succeptible to bugs if the string is short?
		endOfString += 1

#print (bestString)
print ("Longest substring in alphabetical order is: " + (bestString))
