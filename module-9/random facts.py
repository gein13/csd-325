#Scott Chamberlain
#CSD325 - M9.2
#5/11/2026

import requests

response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")

print("Status Code:", response.status_code)

print("\nRaw Response:")
print(response.text)

data = response.json()

print("\nFormatted Response:")
print("Random Useless Fact:")
print(data["text"])
print("Source:", data["source"])