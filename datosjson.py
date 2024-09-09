import json
import yaml

with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)
print (ourjson)
print ("el token de acceso es: {}".format(ourjson['access_token']))
print ("el token expira en {} seconds.".format(ourjson['expires_in']))
