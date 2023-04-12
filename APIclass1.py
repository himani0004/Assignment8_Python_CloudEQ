

#why RSET API is stateless?
#  REST API are stateless because the calls can be made independently of one another, and each call contains
#  all of the data necessary to complete itself successfully.With this rather than relying on the server
#  remembering previous requests, REST applications require each request to contain all of the information
#  necessary for the server to understand. 


# erorrs 403,503,301?
# 403-->when you try to access an API and you do not have the permission to perform the actions required 
# by the API.
#  503---> the server is not ready to handle the request.
# 301--->the server believes that the requested resource is invalid and that the request should be redirected
#  to a new, proper URL.



# Public API usng http methods

#get method(read the data)----------------->>>>>>>>>>>>>>>>>>>>>>>>>>>
import requests
import json
var = "https://jsonplaceholder.typicode.com/todos/10"
response=requests.get(var)
print(type(var))
print(response)
print (response.json())



#post method(to create the data)--------------->>>>>>>>>>>>>>>
data={"userID ":50,"title" :"hello there"}
var1= "https://jsonplaceholder.typicode.com/todos"
response=requests.post(var1,json=data)
print(type(var1))
print(response)
print (response.json())



#put method (update the data)--------------------------->>>>>>>>>>>>>>>>>>
data2={"userID ":2,"title" :"using put method","completed":True}
var2= "https://jsonplaceholder.typicode.com/todos/10"
response=requests.put(var2,json=data2)
print(type(var2))
print(response)
print (response.json())


var7 = "https://jsonplaceholder.typicode.com/todos/10"
response=requests.get(var7)
# print(type(var))
print(response)
print (response.json())






#patch method(to update particular data)----------------------->>>>>>>>>>>>>>>>>>
data3={"title":"hope you doing good"}
var3= "https://jsonplaceholder.typicode.com/todos/10"
response=requests.patch(var3,json=data3)
print(response)
print(response.json())


#delete method(to dlete the data)------------------>>>>>>>>>>>>>>>>>>>>>>>>
var4= "https://jsonplaceholder.typicode.com/todos/10"
response=requests.delete(var4)
print(response)
print (response.json())