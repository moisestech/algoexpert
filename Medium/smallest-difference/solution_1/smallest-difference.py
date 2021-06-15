# Time:   O(n Log(n)) + m Log(m))
# Because we are sorting both array
# We iterate through all the number once

# Space:  O(1)
# Because we are sorting in place
# not storing any additional memory that depends on the length of the input
# thus we are computing in constant space

def smallestDifference(arrayOne, arrayTwo):
	# ask if it's ok to sort arrars in place
	# if we couldnt sort inplace and we had to copy them 
	# then we would need additional space
	arrayOne.sort()
	arrayTwo.sort()
	idxOne = 0
	idxTwo = 0
	smallest = float("inf")
	current = float("inf")
	smallestPair = []

	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
		firstNum = arrayOne[idxOne]
		secondNum = arrayTwo[idxTwo]

		# current = abs(firstNum = secondNum)
		if firstNum < secondNum:
			current = secondNum - firstNum
			idxOne += 1
		elif secondNum < firstNum:
			current = firstNum - secondNum
			idxTwo += 1
		else:
			return [firstNum, secondNum]
		if smallest > current:
			smallest = current
			smallestPair = [firstNum, secondNum]
	return smallestPair
