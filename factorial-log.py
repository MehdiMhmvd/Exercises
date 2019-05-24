#1 usr/bin/python3
import logging
logging.basicConfig(filename = "myProgramLog.txt", level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#1-Debug
#2-INFO
#3-WARNING
#4- ERROR
#5-CRITICAL
#logging.disable(logging.DEBUG)     ##it will disable depends on level that we are passing to it 
#logging.disable(logging.INFO)
#logging.disable(logging.CRITICAL)  ## it will disbal eall the dubuges 

logging.debug('Start of program')

def factorial(n):
	logging.debug('Start of factorial(%s)' %(n))
	total = 1
	for i in range(1 , n + 1):
		total *= i
		logging.debug('i is ' + str(i) + ', total is ' + str(total))
		logging.info("this is logging for info")
	logging.debug('End of factorial(%s)' %(n))
	return total
print(factorial(5))
logging.debug('End of program')