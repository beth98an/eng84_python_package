## Python Packages

### What is a package
- A package is a collection of Python modules.
### Why should we use them 
- Packages allow you to break down large systems and organize their modules in a consistent way that you and other people can use and reuse efficiently
### What is pip
- `pip` is a package manager in Python to install any packages
- To use pip `pip install package_name`
- `pip3 install requests` installs the package requests
```
from random import random # generates random numbers
import math

print(random())

num_float = 23.6
print("actual float value " + str(num_float))
print(math.ceil(num_float))  # ceil() rounds up the value
print(math.floor(num_float))  # floor() rounds down the value
```

### Python Modules
- Modules are Python files which contain a set of functions, classes and variables that can be used within other files.
```
import os
import datetime, sys

working_directory = os.getcwd() # it tells us the current directory location
print(working_directory)

# print(os.uname()) does not work on windows
print(os.cpu_count())
print(datetime.date.today())
print(sys.path)
print(math.pi)
```
### Python requests package
- Connecting to live web using python requests api
- We will connect to www.bbc.com and check if the web is live
```
import requests

responses = requests.get("http://www.bbc.co.uk/")
if responses.status_code == 200:
    print("The website is up and running, status code is " + str(responses.status_code))
else:
    print("oops something went wrong " + str(responses.status_code))
```
- status 200 which means the website is live running
- status 400 or 404 means not working

- Creating a function called status_code_check
- function should return status code with appropriate message
```
def status_code_check(website):
    web = requests.get(website).status_code
    if web == 200:
        print("The website is up and running, status code is " + str(web))
    else:
        print("oops something went wrong " + str(web))


status_code_check("http://www.bbc.co.uk/")
status_code_check("http://www.marvel.com/404")
```
- An alternative method for checking if a website is live.
```
response = requests.get("http://www.bbc.co.uk/")
if response:  # the condition was True
    print("Success" + str(response.status_code))
elif response:
    print("Failure")
elif response:
    print("Oops something went wrong")
```
- Requests, goes one step further in simplifying this process for us.
- If you use response instance in a condition expression it will evaluate to True if the status code was between 200 and 400, and False otherwise.
- Therefore, you can simplify the last example by rewriting the if statement.
