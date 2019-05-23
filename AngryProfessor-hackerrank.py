k = 2  #cancelation threshold
a = [0 ,-1 ,1 ,2]  #arrival time of each student 

def angryProfessor(k, a):
	'''Printiing YES for cancellation 
		No for not cancellation 
		'''
	result = ""
	present = 0
	for item in a:
		if item <= 0:
			present += 1
	if present >= k:
		result = "No"
	else:
		result = "YES"
	return result

print(angryProfessor(k,a))