from fileinput import filename

import cv2
from pyzbar import pyzbar
import os

def decode_qrcode(image_path):
    image = cv2.imread(image_path)

    decoded_objects = pyzbar.decode(image)

    for obj in decoded_objects:
        print("Name", filename)
        print("Type:", obj.type)
        print("Data:", obj.data.decode("utf-8"))

filenames = []

def get_all_filenames_as_string(directory_path):
    try:
        for dirpath, _, files in os.walk(directory_path):
            for file in files:
                filenames.append(file)
    except Exception as e:
        print(f"[ERROER]{e}")
        return ""

get_all_filenames_as_string("images")

for filename in filenames:
    path = "images/" + filename
    decode_qrcode(path)