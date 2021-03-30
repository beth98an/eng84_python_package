# API for postcode.io

import requests

url = "http://api.postcodes.io/postcodes/"
postcode = "e147le"

url_arg = url + postcode
print(url_arg)
response = requests.get(url_arg)
print(response.status_code)
# print(response.content)
# print(response.headers)
# print(response.encoding.isdigit())
# print(response.is_redirect)

response_dict = response.json()
response_keys = response_dict['result']
print(type(response_dict))
for keys in response_keys:
    if keys == "postcode":
        print("Your postcode locations is " + str(response_keys['postcode']))
    if keys == "longitude":
        print("Your longitude is " + str(response_keys["longitude"]))
    elif keys == "latitude":
        print("Your latitude is " + str(response_keys["latitude"]))

    





