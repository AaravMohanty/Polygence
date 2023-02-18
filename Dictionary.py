import csv
import json

def csv_to_coco():
    coco_data = {
        "images": [],
        "annotations": [],
        "categories": [{
                "id": 1,
                "name": "trophy",
                "supercategory": "object",
        }]
    }
    img_id=0
    anot_id =0
    with open('trophyImages.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|' )
        for row in csv_reader:
            c = 0
            if c % 2 != 0:
                # image file name
                image_name = row[0]
                # image coordinates
                print(row)
                # x = row[1]
                # y = row[2]
                # h = row[3]
                # w = row[4]
                image_dict = {
                    'file_name': image_name,
                    'image_id': img_id,
                    'height': 480,
                    'width': 270,
                }
                annotation = {
                    "id": anot_id,
                    "image_id": img_id,
                    "category_id": 1,
                    # "area": h*w,
                    # "bbox": [x, y, w, h],
                    "iscrowd": 0,
                }
                coco_data["images"] += [image_dict]
                coco_data["annotations"] += [annotation]
                c+=1



    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(coco_data, f, ensure_ascii=False, indent=4)



csv_to_coco()