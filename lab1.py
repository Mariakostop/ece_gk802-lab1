import requests
from datetime import datetime

i = input("Give url: ")
r = requests.get(i)
for j in r.headers :
    print(j)
    
print("software: "+r.headers["Server"])

if "Set-Cookie" in r.headers :
    for c in r.cookies :
        print("cookie_name: "+c.name)
        if c.expires==None:
            print("Expire date doesn't exist")
        else:
            exp_date=c.expires
            now=datetime.now().timestamp()
            print("Cookie valid for:"+str(exp_date-now))
            
    
else : print("No cookies")
