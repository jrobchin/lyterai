import requests

url = "http://office:5000/realestateclassifier"

payload = {'image-url': 'https://images.victorianplumbing.co.uk/images/Modern-Bathroom-Suite-img.jpg'}

response = requests.request("POST", url, data=payload)

print(response.text)