import requests

#For one single request

url = 'http://www.omdbapi.com/?t=toy+story&apikey=72bc447a'
r = requests.get(url)
json_data = r.json() #or r.text
print(json_data)


#For multiple requests

url = 'http://www.omdbapi.com/?t=toy+story&apikey=72bc447a'
r = requests.get(url)
json_data = r.json()
for key, value in json_data.items():
    print(key + ':', value)

#the other way to do this last bit is:
for k in json_data.keys():
    print(k + ': ', json_data[k])

    
