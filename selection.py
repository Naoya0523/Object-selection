import cv2
import pandas as pd
import os

filepath = "test-csv.csv"
df = pd.read_csv(filepath)

annotation_csv = pd.DataFrame()

try:
    os.mkdir("Transformed-Images")
except Exception:
    pass

img_folder_path = "Images/"
for row in df.itertuples():
    img_path = img_folder_path + row[1]
    xmin = row[2]
    ymin = row[3]
    xmax = row[4]
    ymax = row[5]
    tag = row[6]

print(img_path, xmin, ymin, xmax, ymax)