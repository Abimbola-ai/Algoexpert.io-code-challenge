def twoNumberSum(array, targetSum):
    # Write your code here.
	for i, v in enumerate(array):
		complementary = targetSum - v
		if complementary in array and i != array.index(complementary):
			return [complementary, v]
	if complementary not in array:
		return []