import sys

filee = sys.argv[1]
try:
	if sys.argv[1][-7:] != '.papple':
		print('Interpreter Error file must have .papple extension')
		sys.exit()
except:
	print('Something happened.')
	sys.exit()
file = open(filee)
fileo = file.read()

if "0123456789".find(fileo[0]) < 0:
	print('Syntax Error first character must be a number')
	sys.exit()

if fileo[1] != 'p':
	print('Syntax Error second character must be \'p\'')
	sys.exit()
	
print(str(fileo[0]) + ''.join([fileo[2:] for s in range(int(fileo[0]))]))