import requests
 
end  = 'http://127.0.0.1:8000/api'
obj = requests.get(end)
print(obj.text)
print(obj.status_code)
print(obj.json()["messgae"])