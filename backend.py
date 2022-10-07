from pyjstat import pyjstat
from urllib import response
import requests


post_url = "https://data.ssb.no/api/v0/no/table/09588/"

payload = {
    "query": [
        {
            "code": "Region",
            "selection": {
                "filter": "vs:Kommune",
                "values": [
                    "3007",
                    "3038",
                    "3047",
                    "3053",
                    "0601",
                    "0605",
                    "0612",
                    "0623",
                    "0532"
                ]
            }
        },
        {
            "code": "ContentsCode",
            "selection": {
                "filter": "item",
                "values": [
                    "Netto"
                ]
            }
        },
        {
            "code": "Tid",
            "selection": {
                "filter": "item",
                "values": [
                    "2004",
                    "2005",
                    "2006",
                    "2007",
                    "2008",
                    "2009",
                    "2010",
                    "2011",
                    "2012",
                    "2013",
                    "2014",
                    "2015",
                    "2016",
                    "2017",
                    "2018",
                    "2019",
                    "2020",
                    "2021"
                ]
            }
        }
    ],
    "response": {
        "format": "json-stat2"
    }
}

response = requests.post(post_url, json=payload)
print(response)


data = pyjstat.Dataset.read(response.text)

print(response.text)
dataframe = data.write('dataframe')
dataframe.head()
dataframe.tail()
dataframe.info()
