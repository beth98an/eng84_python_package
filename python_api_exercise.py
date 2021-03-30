import requests


class Postcode:

    def __init__(self):
        self.url = "http://api.postcodes.io/postcodes/"
        self.name = input("Please enter your name ")
        self.postcode = input(" Please enter your postcode without a space ")

    def greet(self):
        print(f"Hello, {self.name}! Thank you for visiting")

    def status_code_check(self):
        url_arg = self.url + self.postcode
        print(url_arg)
        status = requests.get(url_arg).status_code
        if status == 200:
            print("The website is up and running, status code is " + str(status))
        else:
            print("oops something went wrong " + str(status))

    def check_region(self):
        url_arg = self.url + self.postcode
        response = requests.get(url_arg)
        response_dict = response.json()
        response_keys = response_dict['result']
        for keys in response_keys:
            if keys == "postcode":
                print("Your postcode location is " + str(response_keys['postcode']))
            if keys == "country":
                print("Your country is " + str(response_keys["country"]))


postcode = Postcode()
postcode.greet()
postcode.status_code_check()
postcode.check_region()
