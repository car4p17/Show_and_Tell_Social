#!/usr/bin/python
import json
import csv
import requests
import shutil

if __name__ == '__main__':
    fileToReadFrom = "instagram_json/insta-caption-train.json"
    fileToWriteTo = "train/instagramanns.csv"
    with open(fileToWriteTo, 'w', newline='') as outputfile:
        writer = csv.writer(outputfile, delimiter=",")
        writer.writerow(["", "image_id", "image_file", "caption"])
        with open(fileToReadFrom) as jsonFile:
            data = json.load(jsonFile)
            index = 0
            for user in data:
                for fileName in data[user]:
                    if index < 1001:
                        caption = data[user][fileName]['caption'].replace(",", "")
                        print("Caption: ", caption)
                        try:
                            writer.writerow([index, index, "./train/traininsta/" + user + "_@_" + fileName, caption])
                            index = index + 1
                        except:
                            pass
