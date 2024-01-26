import requests
import json 
end  = 'http://127.0.0.1:8000/Product/Update/2'
obj = requests.put(end,json={"name":"mark",'price':2000})
print(obj.url)
