import re
import string

f = open("input.txt")
line = f.readline()
table = {}
while line:
	if line == '\n':
		break
	else:
		elem = line.split(' ')
		table[elem[1]] = string.atof(elem[3])
		line = f.readline()
print table

results =[]
line = f.readline()
nametable = {'yards':'yard', 'furlongs':'furlong' , 'faths':'fath', 'feet':'foot', 'inches':'inch','miles':'mile'}


def Transform(number, dw):
	if number > 1:
		realname = nametable[dw]
		result = number * table[realname]
		result = float('%0.2f'%result)
	else:
		result = number * table[dw]
		result = float('%0.2f'%result)
	return result



i = 1
while line:
	if i > 6:
		break
	else:
		tup = re.compile(r'([\d\.]+) (\w+)[ -+]?').findall(line)
		number = string.atof(tup[0][0])
		dw = tup[0][1]
		result = Transform(number, dw)
		results.append(result)
		i = i + 1
	line = f.readline()

i = 1
while line:
	if i > 2:
		break
	else:
		js = re.compile(r'([+-])').findall(line)
		tup = re.compile(r'([\d\.]+) (\w+)[ -+]?').findall(line)
		meter = []
		meter.append(Transform(string.atof(tup[0][0]), tup[0][1]))
		meter.append(Transform(string.atof(tup[1][0]), tup[1][1]))
		if js[0][0] == '+':
			result = meter[0] + meter[1]
		else:
			result = meter[0] - meter[1]
		results.append(result)
		i = i + 1
	line = f.readline()

while line:
	if line == '\n':
		break
	else:
		js = re.compile(r'([+-])').findall(line)
		tup = re.compile(r'([\d\.]+) (\w+)[ -+]?').findall(line)
		meter = []
		meter.append(Transform(string.atof(tup[0][0]), tup[0][1]))
		meter.append(Transform(string.atof(tup[1][0]), tup[1][1]))
		meter.append(Transform(string.atof(tup[2][0]), tup[2][1]))

		result = 0
		if js[0][0] == '+':
			result = meter[0] + meter[1]
		else:
			result = meter[0] - meter[1]
		if js[1][0] == '+':
			result = result + meter[2]
		else:
			result = result - meter[2]
		results.append(result)
		line = f.readline()

print results

email = 'liran_elso@163.com'

s = []

for k in range(1,13):
	if k == 1:
		s.append(email + '\n')
	elif k == 2:
		s.append('\n')
	else:
		s.append(str(results[k - 3]) + ' m' + '\n')

file('./output.txt','w').writelines(s)



f.close()



