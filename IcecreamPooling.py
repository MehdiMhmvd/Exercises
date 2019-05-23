m =4
arr = (2,2,4,3)   #2 2 4 3
index = set()
arrdict = {arr[i] : i for i in range(len(arr)) }

keys = list(arrdict.keys())
'''
for i in range(len(arr)):

	for s in range(i+1,len(arr)):
		
		if arr[i] + arr[s] == m:
			print(i)
			print(s)
			print("%d %d"%(arr[i] , arr[s]))


			print("%d %d"%(arr.index(arr[i]) , arr.index(arr[s])))
			
'''





