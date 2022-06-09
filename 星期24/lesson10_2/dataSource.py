import requests
import csv

url = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=642de4f4-cfdf-4c4c-a2f3-e6e6fe1d5343&rid=7d1c0b7a-ba82-445f-ba7c-563d8014b689"

def downloadData():
    filename = "桃園youbike.csv"
    response = requests.get(url)
    if response.status_code == 200:
        file = open(filename,'wb')
        writer = csv.writer(file)
        writer.writerows(response.content.decode("utf-8"))
        file.close()


def parseData():
    pass