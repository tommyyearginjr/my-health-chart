def MyChart():
	import datetime
	date = datetime.datetime.today()
	info = input('Info: ')
	print('{:%Y%m%d%H%M} {}'.format(date,info))
	f = open('MyHealthChart.txt','a')
	f.write('{:%Y%m%d%H%M} {}\n'.format(date,info))
	f.close()
MyChart()
