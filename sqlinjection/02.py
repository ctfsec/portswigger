import requests
from bs4 import BeautifulSoup
import sys

try:
	url = input("Enter the url: ")
	username = input("Enter username / payload: ")
	password = input("Enter password: ")

	headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0'
	}

	with requests.Session() as session:
		#Initial request
		response = session.get(url, headers=headers)
		#print(response.text)

		#Parse the response to find the CSRF token
		soup = BeautifulSoup(response.text, 'html.parser')
		csrf_token_field = soup.find('input', attrs={'name': 'csrf'})
		#print(csrf_token_field)

		#Check if the CSRF token is found
		if csrf_token_field is None:
			print("No CSRF Token Please check your network or URL")
			sys.exit(1)

		#Extract CSRF Token if found
		csrf = csrf_token_field['value']
		print(csrf)

		#Prepare login data
		login_data = {'username':username, 'password':password, 'csrf':csrf}

		#Making a POST Request
		login_response = session.post(url, data=login_data, headers=headers)
		#print(login_response.text)

		#Check for login success
		if "Log out" in login_response.text:
			print("Congratulations, you solved the lab!")

		else:
			print("Invalid username, password or payload")


			
except requests.exceptions.RequestException as e:
	#Handling Network related error in URL
	print(f"Error with the network requests: {e}")
			
except KeyboardInterrupt:
	#Handle the use case where the user interrupt the program (Ctrl+C)
	print("\nProgram Interrupted by user.")
	sys.exit()
