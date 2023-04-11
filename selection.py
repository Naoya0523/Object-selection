import cv2
import pandas as pd
import os

filepath = ""
df = pd.read_csv(filepath)

try:
    os.mkdir("Transformed-Images")
except Exception:
    pass

img_folder_path = ""

def get_img_and_annotations(df):
    num = 0
    list_for_csv = []

    print("processing...")

    for row in df.itertuples():
        value_list = []
        img_path = img_folder_path + row[1]

        #coordinate
        xmin = int(row[2])
        ymin = int(row[3])
        xmax = int(row[4])
        ymax = int(row[5])

        #label
        label = row[6]

        #save the image
        img_name = "img" + str(num) + ".jpg"

        img = cv2.imread(img_path)
        target_img = img[ymin:ymax, xmin:xmax]
        cv2.imwrite("Transformed-Images/" + img_name, target_img)

        #make a list for csv file
        value_list.append(img_name)
        value_list.append(label)
        list_for_csv.append(value_list)

        num += 1

    annotation_csv = pd.DataFrame(list_for_csv, columns=["img", "tag"])
    annotation_csv.to_csv("annotations.csv")
    print("completed!")

if __name__ == "__main__":
    get_img_and_annotations(df)