import os 

try:
    pecUser = os.environ['PEC_USER']
    print('ENV PEC_USER  environment variable exists')
    
    pecPWD  = os.environ['PEC_PASS']
    print('ENV PEC_PASS  environment variable exists')

except KeyError:
    print('ENV environment variable does not exist')
    quit()


def var_check(var):
	try:
		var = os.environ['var']
		print("Running with user: %s" % var)

		#pecUser = os.environ['PEC_USER']
		#pecPWD  = os.environ['PEC_PASS']
		#print("Running with user: %s" % pecUser)
		#print("Running with user: %s" % pecPWD)

	except:
		print("You suck! set PEC_USER/PEC_PASS!!")


