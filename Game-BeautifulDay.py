i = 20
j = 23
k = 6
count = 0
for i in range(i, j+1):
	ii = str(i)
	 if abs(i - int(ii[::-1])) % k == 0:
	 	count += 1



	print("-" * 10)
	print(ii)
	print(a)
