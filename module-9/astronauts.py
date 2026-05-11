#Scott Chamberlain
#CSD325 - M9.2
#5/11/2026

import requests

response = requests.get("http://api.open-notify.org/astros.json")

print("Status Code:", response.status_code)

print("\nRaw Response:")
print(response.text)

data = response.json()

print("\nFormatted Response:")
print("People currently in space:", data["number"])

for person in data["people"]:
    print(person["name"], "-", person["craft"])