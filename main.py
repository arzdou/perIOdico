#venv/bin/python3.8
from datetime import datetime

def main():

	while True:
		try:
			date_str = input("When were you born? (DD-MM-YYYY): ")
			date = datetime.strptime(date_str, '%d-%m-%Y')
			break
		except ValueError:
			print("Date is incorrect, try again")

	url = 'https://elpais.com/hemeroteca/elpais/portadas/{}'.format(date.strftime('%Y/%m/%d')) 
	print(url)

if __name__=="__main__":
	main()