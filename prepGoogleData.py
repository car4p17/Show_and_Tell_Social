#!/usr/bin/python
import csv
import requests
import shutil

if __name__ == '__main__':
    fileToReadFrom = "train/Train_GCC-training.tsv"
    fileToWriteTo = "train/googleanns.csv"
    with open(fileToWriteTo, 'w', newline='') as outputfile:
        writer = csv.writer(outputfile, delimiter=",")
        writer.writerow(["", "image_id", "image_file", "caption"])
        with open(fileToReadFrom) as tsvfile:
            reader = csv.reader(tsvfile, delimiter='\t')
            for i in range(1, 1000):
                row = reader.__next__()
                caption = row[0]
                imageURL = row[1]
                print("caption: ", caption)
                print("imageURL: ", imageURL)
                fileName = './train/traingoogle/' + str(i) + "_" + imageURL.split("/")[-1].split("?")[0]
                try:
                    if not "police" in caption:
                        r = requests.get(imageURL, stream = True)
                        if r.status_code == 200:
                            r.raw.decode_content = True
                            with open(fileName, 'wb+') as f:
                                shutil.copyfileobj(r.raw, f)
                                writer.writerow([i, i, fileName, caption])
                except:
                    print("Skipping")
