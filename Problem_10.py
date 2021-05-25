a = 'Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23
numbers =[]
letters =[]
for i in a:
	if i.isnumeric():
		numbers.append(int(i))
	else:
		letters.append(i)
		print(numbers,'\n',letters