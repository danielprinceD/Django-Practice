import requests
 
end  = 'http://127.0.0.1:8000/Product/ViewData/1'
obj = requests.get(end)
print(obj.url)
print(obj.json())