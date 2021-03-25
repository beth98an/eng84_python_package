# Python requests package
# Let's connect to live web using python requests api
# we will connect to www.bbc.com and check if the web is live

import requests

responses = requests.get("http://www.bbc.co.uk/")
if responses.status_code == 200:
    print("The website is up and running, status code is " + str(responses.status_code))
else:
    print("oops something went wrong " + str(responses.status_code))
# status 200 which means the website is live running
# status 400 or 404 means not working


# create a function called status code check
# function should return status code with appropriate message
# DRY
def status_code_check(website):
    web = requests.get(website).status_code
    if web == 200:
        print("The website is up and running, status code is " + str(web))
    else:
        print("oops something went wrong " + str(web))


status_code_check("http://www.bbc.co.uk/")
status_code_check("http://www.marvel.com/404")

response = requests.get("http://www.bbc.co.uk/")
if response:  # the condition was True
    print("Success" + str(response.status_code))
elif response:
    print("Failure")
elif response:
    print("Oops something went wrong")
# requests goes one step further in simplifying this process for us
# if you use response instance in a condition expression
# it will evaluate to True if the status code was between 200 and 400, False otherwise
# therefore, you can simplify the last example by rewriting the if statement

