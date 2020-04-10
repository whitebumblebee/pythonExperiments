# # from jsonschema import validate
# from genson import SchemaBuilder
# import json
# import requests
# from check_api import (
#     indianApiUrlList,
#     deepsetUrlList,
#     globalUrlList,
# )

# # Globals
# # indianApiUrl = ['IndianApi','https://api.covid19india.org/data.json','IndianApiCurrentSchema']
# # globalApiUrl = ['globalApi','https://corona.lmao.ninja/all','globalApiCurrentSchema']
# # globalApiCountriesUrl = ['globalApi --> Countries','https://corona.lmao.ninja/countries','globalApiCountriesCurrentSchema']
# # globalApiUsaUrl = ['globalApi --> USA','https://corona.lmao.ninja/countries/USA','globalApiUSACurrentSchema']
# # deepsetApiFaqUrl = ['DeepsetApi --> FAQ','https://covid-backend.deepset.ai/models/1/faq-qa','deepSetApiFaqCurrentSchema']
# # deepsetApiFeedbackUrl = ['DeepSetApi --> Feedback','https://covid-backend.deepset.ai/models/1/feedback','deepSetApiFeedbackCurrentSchema']
# # indianApiUrlList = [indianApiUrl]
# # globalUrlList = [globalApiUrl,globalApiCountriesUrl,globalApiUsaUrl]
# # deepsetUrlList =[deepsetApiFaqUrl,deepsetApiFeedbackUrl]

# def apiCheck(latestSchema,UrlType):
#     with open('{}.txt'.format(UrlType[2]),'r+') as f:
#         currentSchema = f.read()
#         if currentSchema == latestSchema:
#             return "JSON Structure/Schema is already upto date for {} U+2714".format(UrlType[0])
#         else:
#             # return "JSON Structure/Schema has been changed for {} U+2757".format(UrlType[0])
#             f.write(latestSchema)
#             return "Schema Updated for {} U+2714".format(UrlType[0])

# def main(indianApiUrlList,globalUrlList,deepsetUrlList):
#     for i in globalUrlList:
#         resp = requests.get(i[1])
#         data = resp.json()
#         builder = SchemaBuilder()
#         builder.add_object(data)
#         latestSchema = json.dumps(builder.to_json())
#         # apiStatus = statusCheck(resp,i)
#         # print(apiStatus)
#         api_check = apiCheck(latestSchema,i)
#         print(api_check)
#         print("\n\n")
#     for i in deepsetUrlList:
#         resp = requests.get(i[1])
#         data = resp.json()
#         builder = SchemaBuilder()
#         builder.add_object(data)
#         latestSchema = json.dumps(builder.to_json())
#         # apiStatus = statusCheck(resp,i)
#         # print(apiStatus)
#         api_check = apiCheck(latestSchema,i)
#         print(api_check)
#         print("\n\n")
#     for i in indianApiUrlList:
#         resp = requests.get(i[1])
#         data = resp.json()
#         builder = SchemaBuilder()
#         builder.add_object(data)
#         latestSchema = json.dumps(builder.to_json())
#         # apiStatus = statusCheck(resp,i)
#         # print(apiStatus)
#         api_check = apiCheck(latestSchema,i)
#         print(api_check)
#         print("\n\n")

# if __name__ == '__main__':
#     main(indianApiUrlList,globalUrlList,deepsetUrlList)



# from jsonschema import validate
# from genson import SchemaBuilder
# import json
# import requests
# from check_api import (
#     indianApiUrlList,
#     deepsetUrlList,
#     globalUrlList,
# )


# def updateSchema(data,latestSchema,UrlType):
#     with open('{}.json'.format(UrlType[2]),'r') as f:
#         currentSchema = json.loads(f.read())
#         # if currentSchema == latestSchema:
#         #     return "JSON Structure/Schema is upto date for {} U+2714".format(UrlType[0])
#         # else:
#         #     return "JSON Structure/Schema has been changed for {} U+2757".format(UrlType[0])
#         try:
#             validate(instance=data,schema=currentSchema)
#             return "JSON schema is up to date"
#         except:
#             return "JSON schema is not up to date"
#     # with open('{}.json'.format(UrlType[2]),'r') as f:
#     #     currentSchema = json.loads(f.read())
#     #     # if currentSchema == latestSchema:
#     #     #     return "JSON Structure/Schema is already upto date for {} U+2714".format(UrlType[0])
#     #     # else:
#     #     #     f.write(latestSchema)
#     #     #     return "Schema Updated for {} U+2714".format(UrlType[0])
    
#     #     try:
#     #         validate(instance=data,schema=currentSchema)
#     #         return "JSON Structure/Schema is already upto date for {}".format(UrlType[0])
#     #     except:
#     #         print("Hi")
#             # with open('{}.json'.format(UrlType[2]),'w') as f:
            
#             #     f.write(latestSchema)
#             #     return "Schema Updated for {}".format(UrlType[0])
# def main(indianApiUrlList,globalUrlList,deepsetUrlList):
#     for i in globalUrlList:
#         resp = requests.get(i[1])
#         data = resp.json()
#         builder = SchemaBuilder()
#         builder.add_object(data)
#         latestSchema = builder.to_json()
#         schema_update = updateSchema(data,latestSchema,i)
#         print(schema_update)
#         print("\n\n")
#     for i in deepsetUrlList:
#         resp = requests.get(i[1])
#         data = resp.json()
#         builder = SchemaBuilder()
#         builder.add_object(data)
#         latestSchema = builder.to_json()
#         schema_update = updateSchema(data,latestSchema,i)
#         print(schema_update)
#         print("\n\n")
#     for i in indianApiUrlList:
#         resp = requests.get(i[1])
#         data = resp.json()
#         builder = SchemaBuilder()
#         builder.add_object(data)
#         latestSchema = builder.to_json()
#         schema_update = updateSchema(data,latestSchema,i)
#         print(schema_update)
#         print("\n\n")

# if __name__ == '__main__':
#     main(indianApiUrlList,globalUrlList,deepsetUrlList)

# # from jsonschema import validate
# from genson import SchemaBuilder
# import json
# import requests

# # Globals
# indianApiUrl = ['IndianApi','https://api.covid19india.org/data.json','IndianApiCurrentSchema']
# globalApiUrl = ['globalApi','https://corona.lmao.ninja/all','globalApiCurrentSchema']
# globalApiCountriesUrl = ['globalApi --> Countries','https://corona.lmao.ninja/countries','globalApiCountriesCurrentSchema']
# globalApiUsaUrl = ['globalApi --> USA','https://corona.lmao.ninja/countries/USA','globalApiUSACurrentSchema']
# deepsetApiFaqUrl = ['DeepsetApi --> FAQ','https://covid-backend.deepset.ai/models/1/faq-qa','deepSetApiFaqCurrentSchema']
# deepsetApiFeedbackUrl = ['DeepSetApi --> Feedback','https://covid-backend.deepset.ai/models/1/feedback','deepSetApiFeedbackCurrentSchema']
# indianApiUrlList = [indianApiUrl]
# globalUrlList = [globalApiUrl,globalApiCountriesUrl,globalApiUsaUrl]
# deepsetUrlList =[deepsetApiFaqUrl,deepsetApiFeedbackUrl]

# # Function for checking individual api..
# def apiCheck(latestSchema,UrlType):
#     with open('{}.txt'.format(UrlType[2]),'r') as f:
#         currentSchema = f.read()
#         if currentSchema == latestSchema:
#             return "JSON Structure/Schema is upto date for {} U+2714".format(UrlType[0])
#         else:
#             return "JSON Structure/Schema has been changed for {} U+2757".format(UrlType[0])

# def statusCheck(response,urlType):
#     if response.status_code == 200:
#         return "Api is up and running for {} U+2714".format(urlType[0])
#     if response.status_code == 301:
#         return "The url for api has changed for {} U+26A0".format(urlType[0])
#     if response.status_code == 400:
#         return "bad request for {} U+26A0".format(urlType[0])
#     if response.status_code == 401:
#         return "Authentication problem for {} U+26A0".format(urlType[0])
#     if response.status_code == 403:
#         return "Forbidden request for {} U+26A0".format(urlType[0])
#     if response.status_code == 404:
#         return "Resource not found for {} U+26A0".format(urlType[0])
#     if response.status_code == 503:
#         return "Server not ready handle the request for {} U+26A0".format(urlType[0])
#     else:
#         return "{} response was returned U+26A0".format(response.status_code)

# def main(indianApiUrlList,globalUrlList,deepsetUrlList):
#     for i in globalUrlList:
#         resp = requests.get(i[1])
#         data = resp.json()
#         builder = SchemaBuilder()
#         builder.add_object(data)
#         latestSchema = json.dumps(builder.to_json())
#         apiStatus = statusCheck(resp,i)
#         print(apiStatus)
#         api_check = apiCheck(latestSchema,i)
#         print(api_check)
#         print("\n\n")
#     for i in deepsetUrlList:
#         resp = requests.get(i[1])
#         data = resp.json()
#         builder = SchemaBuilder()
#         builder.add_object(data)
#         latestSchema = json.dumps(builder.to_json())
#         apiStatus = statusCheck(resp,i)
#         print(apiStatus)
#         api_check = apiCheck(latestSchema,i)
#         print(api_check)
#         print("\n\n")
#     for i in indianApiUrlList:
#         resp = requests.get(i[1])
#         data = resp.json()
#         builder = SchemaBuilder()
#         builder.add_object(data)
#         latestSchema = json.dumps(builder.to_json())
#         apiStatus = statusCheck(resp,i)
#         print(apiStatus)
#         api_check = apiCheck(latestSchema,i)
#         print(api_check)
#         print("\n\n")

# if __name__ == '__main__':
#     main(indianApiUrlList,globalUrlList,deepsetUrlList)
        
# builder = SchemaBuilder()
# resp = requests.get('https://api.covid19india.org/data.json')
# data = resp.json()
# builder.add_object(data)
# textData = json.dumps(builder.to_json())
# # print(json.loads(textData))
# with open('./deepSetApiFeedbackCurrentSchema2.txt','w+') as firstFile:
#     content = firstFile.write(textData)
    # print(content)
# import requests
# import json

# resp = requests.get("https://api.covid19india.org/data.json")
# # resp = requests.get("https://corona.lmao.ninja/")
# d = statusCheck(resp)
# print(d)

# data = jsonresp.json()
# for i in data:
#     print(i)
# print(isinstance(data,dict))

# for i in resp.json().keys():
#     print(i)

# for i in d['statewise']:
#     print(i)

# currentCovidIndiaSchema = None

# resp = requests.get("https://covid-backend.deepset.ai/models/1/faq-qa")
# print(isinstance(resp.json(),dict))
# data = resp.json()
# builder.add_object(data)
# print(json.dumps(builder.to_json()))

# schema = {
#      "type" : "object",
#      "properties" : {
#          "price" : {"type" : "number"},
#          "name" : {"type" : "string"},
#      },
#  }
# try:
#     validate(instance={"name" : "Eggs", "price" : "Invalid"}, schema=schema,)  
# except:
#     print("invalid json")







from jsonschema import validate
from genson import SchemaBuilder
import json
import requests

# Globals
# indianApiUrl = ['IndianApi','https://api.covid19india.org/data.json','IndianApiCurrentSchema']
# globalApiUrl = ['globalApi','https://corona.lmao.ninja/all','globalApiCurrentSchema']
# globalApiCountriesUrl = ['globalApi --> Countries','https://corona.lmao.ninja/countries','globalApiCountriesCurrentSchema']
# globalApiUsaUrl = ['globalApi --> USA','https://corona.lmao.ninja/countries/USA','globalApiUSACurrentSchema']
# deepsetApiFaqUrl = ['DeepsetApi --> FAQ','https://covid-backend.deepset.ai/models/1/faq-qa','deepSetApiFaqCurrentSchema']
# deepsetApiFeedbackUrl = ['DeepSetApi --> Feedback','https://covid-backend.deepset.ai/models/1/feedback','deepSetApiFeedbackCurrentSchema']
# indianApiUrlList = [indianApiUrl]
# globalUrlList = [globalApiUrl,globalApiCountriesUrl,globalApiUsaUrl]
# deepsetUrlList =[deepsetApiFaqUrl,deepsetApiFeedbackUrl]
from check_api import (
    indianApiUrlList,
    deepsetUrlList,
    globalUrlList,
)

# Function for checking individual api..
def schemaUpdate(data,latestSchema,UrlType):
    with open('{}.json'.format(UrlType[2]),'r') as f:
        currentSchema = json.loads(f.read())
        # if currentSchema == latestSchema:
        #     return "JSON Structure/Schema is upto date for {} U+2714".format(UrlType[0])
        # else:
        #     return "JSON Structure/Schema has been changed for {} U+2757".format(UrlType[0])
        try:
            validate(instance=data,schema=currentSchema)
            return "JSON Structure/Schema is already upto date for {}".format(UrlType[0])
        except:
            # return "JSON schema is not up to date"
            with open('{}.json'.format(UrlType[2]),'w') as f:
            
                f.write(latestSchema)
                return "Schema Updated for {}".format(UrlType[0])
# def schemaUpdate(data,latestSchema):
#     with open('x.json','r') as f:
#         currentSchema = json.loads(f.read())
#         # if currentSchema == latestSchema:
#         #     return "JSON Structure/Schema is upto date for {} U+2714".format(UrlType[0])
#         # else:
#         #     return "JSON Structure/Schema has been changed for {} U+2757".format(UrlType[0])
#         try:
#             validate(instance=data,schema=currentSchema)
#             return "JSON Structure/Schema is already upto date"
#         except:
#             # return "JSON schema is not up to date"
#             with open('x.json','w') as f:
            
#                 f.write(latestSchema)
#                 return "Schema Updated..."

# def statusCheck(response,urlType):
#     if response.status_code == 200:
#         return "Api is up and running for {} U+2714".format(urlType[0])
#     if response.status_code == 301:
#         return "The url for api has changed for {} U+26A0".format(urlType[0])
#     if response.status_code == 400:
#         return "bad request for {} U+26A0".format(urlType[0])
#     if response.status_code == 401:
#         return "Authentication problem for {} U+26A0".format(urlType[0])
#     if response.status_code == 403:
#         return "Forbidden request for {} U+26A0".format(urlType[0])
#     if response.status_code == 404:
#         return "Resource not found for {} U+26A0".format(urlType[0])
#     if response.status_code == 503:
#         return "Server not ready handle the request for {} U+26A0".format(urlType[0])
#     else:
#         return "{} response was returned U+26A0".format(response.status_code)

def main(indianApiUrlList,globalUrlList,deepsetUrlList):
    for i in globalUrlList:
        resp = requests.get(i[1])
        data = resp.json()
        builder = SchemaBuilder()
        # builder.add_object(data)
        # latestSchema = json.dumps(builder.to_json())
        # apiStatus = statusCheck(resp,i)
        # print(apiStatus)
        builder.add_object(data)
        latestSchema = builder.to_json()
        schema_update = schemaUpdate(data,latestSchema,i)
        print(schema_update)
        # api_check = schemaUpdate(data,i)
        # print(api_check)
        print("\n\n")
    for i in deepsetUrlList:
        resp = requests.get(i[1])
        data = resp.json()
        builder = SchemaBuilder()
        # builder.add_object(data)
        # latestSchema = json.dumps(builder.to_json())
        # apiStatus = statusCheck(resp,i)
        # print(apiStatus)builder = SchemaBuilder()
        builder.add_object(data)
        latestSchema = builder.to_json()
        schema_update = schemaUpdate(data,latestSchema,i)
        print(schema_update)

        # api_check = schemaUpdate(data,i)
        # print(api_check)
        print("\n\n")
    for i in indianApiUrlList:
        resp = requests.get(i[1])
        data = resp.json()
        builder = SchemaBuilder()
        # builder.add_object(data)
        # latestSchema = json.dumps(builder.to_json())
        # apiStatus = statusCheck(resp,i)
        # print(apiStatus)
        builder.add_object(data)
        latestSchema = builder.to_json()
        schema_update = schemaUpdate(data,latestSchema,i)
        print(schema_update)
        # api_check = schemaUpdate(data,i)
        # print(api_check)
        print("\n\n")

# def main2():
#     resp = requests.get('https://api.covid19india.org/data.json')
#     data = resp.json()
#     builder = SchemaBuilder()
#         # builder.add_object(data)
#         # latestSchema = json.dumps(builder.to_json())
#         # apiStatus = statusCheck(resp,i)
#         # print(apiStatus)
#     builder.add_object(data)
#     latestSchema = builder.to_json()
#     schema_update = schemaUpdate(data,latestSchema)
#     print(schema_update)
#     # api_check = schemaUpdate(data,i)
#     # print(api_check)
#     print("\n\n")

if __name__ == '__main__':
    main(indianApiUrlList,globalUrlList,deepsetUrlList)
    # main2()

