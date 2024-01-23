import requests
 
end  = 'http://127.0.0.1:8000/api/post'
obj = requests.post(end,json={'name':'Hello','price':20})
print(obj.url)
print(obj.json())