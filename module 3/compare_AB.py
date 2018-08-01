varA=int(input('enter value'))
varB=int(input('enter value'))
if type(varA)==str or type(varB)==str:
	print('string involved')
elif varA>varB:
	print ('Bigger')
elif varA==varB:
	print('equal')
else:
	print('Smaller')
