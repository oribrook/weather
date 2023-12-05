import requests

print("hi")

res = requests.get("https://genericgs.com")
print(res.text)

print("by")