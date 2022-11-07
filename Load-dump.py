# json is javascript object notation
# Mostly used to store and transfer the data
###########################Deserialization################################
# json.load() - takes json encoded data from a file and converts to python dictionary
# difference between load() and loads():
# json.loads() is used to read json string and returns dictionary.
# example:

# create json file:
# import json
# data = {
# 	"id":"001",
# 	"name":"Shweta",
# 	"password":"ssc",
# }
#
# with open("data_file1.json","w") as file1:
# 	json.dump(data,file1)    #dump(data to be stored,filename to which file is stored)
#
#
# # now load() to convert json FILE to dict
# with open("data_file1.json",'r') as read:
# 	print(json.load(read))


# using loads:
# This is used to parse valid json string to dict.(deserializing)
# import json
# data1 = """{
# 	"id":"001",
# 	"name":"Shweta",
# 	"password":"ssc"
# 	}"""
#
# res = json.loads( data1 )
# print(res)


####################################Serialization########################
# Serialization is converting naive data to json object.
# Dict is converted to json object.
# list tuple converted to json array and
# int, float converted to json number
# None converted to Null

# for serialization we use dump and dumps:
# when we have to write dict to json file we use dump.
# when to convert python object to json string use dumps
# dump takes 2 parameters: json.dump(dict,file_pointer)


# dump():
# import json
# data = {
#     "id":"011",
#     "name":"abc",
#     "pass":"xyz"
# }
#
# with open('d1.json','w') as a:
#     json.dump(data,a)

# dumps:
# import json
# data2 = {
#     "id":"002",
#     "name":"ssc",
#     "pass":"acc"
#     }
# res1 = json.dumps(data2)
# print(res1)





