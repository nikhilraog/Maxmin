
#Script to get min and max as a list in 3n/2 - 2 time complexity
#===============================================================


def minmax(arr):
 
	#mini,maxi;
	if (len(arr) == 1):
		mini = maxi = arr[0]
		return (mini,maxi);
 
	if (len(arr) == 2):
		if arr[0]<arr[1]:
			mini = arr[0]
			maxi = arr[1]
		else:
			mini = arr[1]
			maxi = arr[0]
		return (mini,maxi)
 
 
	ml = minmax(arr[:len(arr)/2])
	mr = minmax(arr[(len(arr)/2)+1:])
 
	if (ml[0] < mr[0]):
		mini = ml[0]
	else: 
		mini = mr[0]
 
	if (ml[1] < mr[1]):
		maxi = mr[1]
	else:
		maxi = ml[1]
 
	return (mini,maxi)


#test data 
#===============================================================================
arr = [25,56,89,91,5,12,122,8,2.2]*100
 
temp = minmax(arr)
print temp
