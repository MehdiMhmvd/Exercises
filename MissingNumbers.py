'''
this program get the list of numbers and compair it with the missing list and 
return the missing items s
'''

arr = [203, 205, 206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

OValues = {}
NewValues = {}
diff = []

for i in range(len(brr)):
	OValues[brr[i]] = brr.count(brr[i])
for n in range(len(arr)):
	NewValues[arr[n]] = arr.count(arr[n])
	
for item in NewValues:
	if NewValues[item] != OValues[item]:
		d = OValues[item] - NewValues[item]
		for i in range(d):
			diff.append(item)



 
print(diff)
print(NewValues)	
print(OValues)
