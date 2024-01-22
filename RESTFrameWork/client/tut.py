import requests
 
end  = 'http://127.0.0.1:8000/api'
obj = requests.get(end,params={'this_is_param':'get_method'},json={'query':'Hello'})
print(obj.url)
print(obj.json())