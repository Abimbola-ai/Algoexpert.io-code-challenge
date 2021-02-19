def isValidSubsequence(array, sequence):
    # Write your code here.
	result = True
    for i in sequence:
        if i in array:
            array = array[array.index(i)+1:]
        else:
            return False
    return result
			