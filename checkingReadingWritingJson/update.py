# from jsonschema import validate
from genson import SchemaBuilder
import json
import requests
from check_api import (
    indianApiUrlList,
    deepsetUrlList,
    globalUrlList,
)

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

def apiCheck(latestSchema,UrlType):
    with open('{}.txt'.format(UrlType[2]),'r+') as f:
        currentSchema = f.read()
        if currentSchema == latestSchema:
            return "JSON Structure/Schema is already upto date for {} U+2714".format(UrlType[0])
        else:
            # return "JSON Structure/Schema has been changed for {} U+2757".format(UrlType[0])
            f.write(latestSchema)
            return "Schema Updated for {} U+2714".format(UrlType[0])

def main(indianApiUrlList,globalUrlList,deepsetUrlList):
    for i in globalUrlList:
        resp = requests.get(i[1])
        data = resp.json()
        builder = SchemaBuilder()
        builder.add_object(data)
        latestSchema = json.dumps(builder.to_json())
        # apiStatus = statusCheck(resp,i)
        # print(apiStatus)
        api_check = apiCheck(latestSchema,i)
        print(api_check)
        print("\n\n")
    for i in deepsetUrlList:
        resp = requests.get(i[1])
        data = resp.json()
        builder = SchemaBuilder()
        builder.add_object(data)
        latestSchema = json.dumps(builder.to_json())
        # apiStatus = statusCheck(resp,i)
        # print(apiStatus)
        api_check = apiCheck(latestSchema,i)
        print(api_check)
        print("\n\n")
    for i in indianApiUrlList:
        resp = requests.get(i[1])
        data = resp.json()
        builder = SchemaBuilder()
        builder.add_object(data)
        latestSchema = json.dumps(builder.to_json())
        # apiStatus = statusCheck(resp,i)
        # print(apiStatus)
        api_check = apiCheck(latestSchema,i)
        print(api_check)
        print("\n\n")

if __name__ == '__main__':
    main(indianApiUrlList,globalUrlList,deepsetUrlList)
