import requests
from bs4 import BeautifulSoup

# URL of the website to hack
url = 'https://pakistan.com/'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all email addresses on the page
emails = []
for link in soup.find_all('a'):
    if 'mailto:' in link.get('href', ''):
        emails.append(link.get('href').replace('mailto:', ''))

# Find all password inputs on the page
passwords = []
for input_tag in soup.find_all('input'):
    if input_tag.get('type') == 'password':
        passwords.append(input_tag.get('value'))

# Print the collected email addresses and passwords
print("Collected Emails:")
for email in emails:
    print(email)

print("\nCollected Passwords:")
for password in passwords:
    print(password)