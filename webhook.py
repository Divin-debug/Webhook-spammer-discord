import requests 
import os 

os.system('color 6')
os.system('cls')
print("To stop press CTRL + C")
print("github.com/Divin-debug")


url = input("Put the whebhook to spam here : ")


data = {
    "content" : "ouga bouga",
    "username" : "gros noir"
}


data["embeds"] = [
    {
        "" : "text in embed",
        "" : "embed title"
    }
]
while True:
	result = requests.post(url, json = data)
 

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))

print("To stop press CTRL + C")
print("github.com/Divin-debug")