import requests
 
end  = 'https://httpbin.org'
obj = requests.get(end)
print(obj.json())