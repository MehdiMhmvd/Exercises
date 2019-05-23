n = 50
shared = 5
comulative = 0
for i in range (1 ,n+1):
	liked = round (shared / 2)
	comulative += liked
	shared = liked * 3
	print("day %d = %d"%(i, comulative) )