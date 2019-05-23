'''
this program get the list of numbers and compair it with the missing list and 
return  sorted the missing items 

'''

#arr = [203, 205, 206, 207, 208, 203, 204, 205, 206]
#brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]
arr = [11, 4, 11, 7, 13, 4 ,12 ,11 ,10 ,14]
brr = [11, 4 ,11,8, 7 ,3,3, 7, 10, 13,13, 4, 8, 12, 11, 10,8 ,14, 12]


OValues = {}
NewValues = {}
diff = []

for i in range(len(brr)):
	OValues[brr[i]] = brr.count(brr[i])
for n in range(len(arr)):
	NewValues[arr[n]] = arr.count(arr[n])
	
for item in OValues:
	if item  not in NewValues.keys():
		for m in range(OValues[item]):
			diff.append(item)
	elif NewValues[item] != OValues[item]:
		d = OValues[item] - NewValues[item]
		for i in range(d):
			diff.append(item)



 
print(sorted(diff))
print(NewValues)	
print(OValues)
