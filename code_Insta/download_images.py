import requests
import cv2
import os 
import numpy as np
import os

def download_images(image_url, im_name):
    file_path = f"images/original_images/{im_name}"
    try:
        response = requests.get(image_url, timeout=10)
        print('response :', response.status_code)
        if response.status_code == 200:
            nparr = np.frombuffer(response.content, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            img = cv2.resize(img, (256, 256))
            cv2.imwrite(file_path, img)
            print(f"✅ Downloaded and saved: {file_path}")
            return True
        else:
            print(f"❌ Failed to download {im_name}")
            return False
    except Exception as e:
        print(f"❌ Error for image {im_name}: {str(e)}")
        return False


def download_all_images(collection):
    for i, doc in enumerate(collection.find()):
        short_code = doc.get("shortCode")
        image_url = doc.get("displayUrl")

        if not short_code or not image_url:
            print(f"⚠️ Skipping document {i} — Missing 'shortCode' or 'displayUrl'")
            continue

        image_name = f"{short_code}.jpg"
        original_path = os.path.join("images/original_images", image_name)

        if os.path.exists(original_path):
            print(f"[{i}] ✅ Already exists: {image_name}")
            continue

        print(f"[{i}] ⬇️ Downloading: {image_name}")
        success = download_images(image_url, image_name)
        if not success:
            print(f"[{i}] ❌ Failed: {image_name}")

