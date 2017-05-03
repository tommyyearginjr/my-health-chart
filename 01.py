def MyChart():
	date = input('Date: ')
	info = input('Info: ')
	print('{} {}'.format(date,info))
	f = open('MyHealthChart.txt','a')
	f.write('{} {}\n'.format(date,info))
	f.close()
MyChart()
