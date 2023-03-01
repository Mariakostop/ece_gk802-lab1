import requests

i = input("give an url: ")
r = requests.get(i)
for j in r.headers :
    print(j)
    
