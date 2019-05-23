#s = ["1", "1","100", "2", "3084193741082937","3084193741082938",'111','200']
unsorted = ["1","1","2","2"]
'''
#print(sorted(s))
sdict = {}
for i in range(len(s)) :
	sdict[i] = int(s[i])
so=sorted(list (sdict.values()))
'''
ssorted = sorted(unsorted,key = int)

print(ssorted)
