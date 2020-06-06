#!/usr/bin/python
import csv

if __name__ == '__main__':
    fileToReadFrom = "Train_GCC-training.tsv"
    with open(fileToReadFrom) as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        ind = 0
        for row in reader:
            ind = ind + 1
            if ind < 1001:
                caption = row[0]
                imageURL = row[1]
                print("caption: ", caption)
                print("imageURL: ", imageURL)