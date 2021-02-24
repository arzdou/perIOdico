#venv/bin/python3.8
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import shutil

import sys
import subprocess


def get_date():
	while True:
		try:
			date_str = input("When were you born? (DD-MM-YYYY): ")
			date = datetime.strptime(date_str, '%d-%m-%Y')
			return date
		except ValueError:
			print("Date is incorrect, try again")


class perIOdico:
	def __init__(date, verbose=False):
		self.verbose = verbose
		str_date = date.strftime('%Y/%m/%d')
		self.url = 'https://elpais.com/hemeroteca/elpais/portadas/{}'.format(date_str) 

	def get_image():
		self.response = requests.get(url)

		soup = BeautifulSoup(response.content, 'html.parser')
		image_url = soup.find_all('img')[0].get('src')

		self.image = requests.get(image_url, stream=True)

		if image_response.status_code == 200:
			with open("img.jpg", 'wb') as f:
				image_response.raw.decode_content = True
				shutil.copyfileobj(image_response.raw, f)
		else:
			if self.verbose:
				print("I could not find first page for that day")
			return

		if self.verbose:
			print("Extracted correctly")

	if sys.platform.startswith('linux'):
        ret_code = subprocess.call(['xdg-open', something_to_open])

    elif sys.platform.startswith('darwin'):
        ret_code = subprocess.call(['open', something_to_open])

    elif sys.platform.startswith('win'):
        ret_code = subprocess.call(['start', something_to_open], shell=True)