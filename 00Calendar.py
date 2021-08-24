import calendar

def main():
	for m in range(8,9):
		cal = calendar.monthcalendar(2021,m)
		#Aug 2021 Days Calendar Array
		print(cal)

	#Time now
	from datetime import datetime
	now=datetime.now()
	print(now.strftime("%d-%b-%Y %H:%M:%S"))

if __name__=="__main__":
	main()
