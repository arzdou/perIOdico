#venv/bin/python3.8
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import shutil

def main():

	while True:
		try:
			date_str = input("When were you born? (DD-MM-YYYY): ")
			date = datetime.strptime(date_str, '%d-%m-%Y')
			break
		except ValueError:
			print("Date is incorrect, try again")

	url = 'https://elpais.com/hemeroteca/elpais/portadas/{}'.format(date.strftime('%Y/%m/%d')) 
	response = requests.get(url)

	soup = BeautifulSoup(response.content, 'html.parser')
	image_url = soup.find_all('img')[0].get('src')

	image_response = requests.get(image_url, stream=True)

	if image_response.status_code == 200:
		with open("first_page.jpg", 'wb') as f:
			image_response.raw.decode_content = True
			shutil.copyfileobj(image_response.raw, f)
	else:
		print("I could not find first page for you that day")
		return

	print("Extracted correctly")

if __name__=="__main__":
	main()