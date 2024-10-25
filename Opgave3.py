import csv
import os

if os.path.exists("Opgave3/source_data.csv"):
    with open("Opgave3/source_data.csv", mode = "r") as fileK:
        csvFile = csv.reader(fileK)
        fileD = open("Opgave3/desSourceData.csv", "w", newline='')
        for lines in csvFile:
            writer = csv.writer(fileD)
            writer.writerows(lines)

else:
    print("File does not exist!!!")
