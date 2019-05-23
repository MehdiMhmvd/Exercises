arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

itemValues = {}
for i in range(len(brr)):
	itemValues[brr[i]] = brr.count(brr[i])

print(itemValues)
