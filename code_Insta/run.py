from pymongo import MongoClient
import pandas as pd
import os
from sentiment_analysis import predict_sentiment
from segment import segment
from devide import devide_into_clusters
from download_images import download_all_images
from HDBSCAN_clusters import hdbscan_clustering
from encode_image import encode
from scrap_insta_data import scrap_insta_data

# Ensure required folders exist
for folder in ["images/original_images", "images/segmented_images", "downloaded_images", "temp", "data"]:
    os.makedirs(folder, exist_ok=True)

# MongoDB setup
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["instagram_data"]
collection = db["posts"]

#=================== Scrap Instagram Data ===================
print("Scraping Instagram data... This may take a while.")
scrap_insta_data()

# download images ================
print("Downloading images...")
download_all_images(collection)


# Load checkpoint if exists
checkpoint_file = "temp/fashion_progress.pkl"
if os.path.exists(checkpoint_file):
    df_checkpoint = pd.read_pickle(checkpoint_file)
    records = df_checkpoint.to_dict(orient="records")
    processed_ids = set(df_checkpoint.get("image_name", []))
    print(f"🔁 Resuming from checkpoint with {len(processed_ids)} processed entries.")
else:
    records = []
    processed_ids = set()

# Process loop
counter = len(processed_ids)
for doc in collection.find():
    image_name = f"{doc['shortCode']}.jpg"
    if image_name in processed_ids:
        continue

    original_path = f'images/original_images/{image_name}'
    segmented_path = f'images/segmented_images/outfit_{image_name}'

    if not os.path.exists(original_path):
        print(f"Skipping {image_name} — image not found.")
        continue

    try:
        if not os.path.exists(segmented_path):
            segment(original_path)
    except Exception as e:
        print(f"Skipping {image_name} — segmentation failed: {e}")
        continue

    try:
        encoded = encode(image_name)
        if encoded is None:
            print(f"Skipping {image_name} — encoding failed.")
            continue
    except Exception as e:
        print(f"Skipping {image_name} — encoding error: {e}")
        continue

    comments = [c["text"] for c in doc.get("latestComments", [])]
    pos, neg, neu = 0, 0, 0
    for c in comments:
        label = predict_sentiment(c)
        if label == 2:
            pos += 1
        elif label == 1:
            neg += 1
        elif label == 0:
            neu += 1

    record = {
        "image_name": image_name,
        "platform": "instagram",
        "page": doc.get("inputUrl", "").rstrip("/").split("/")[-1],
        "latent_vector": encoded,
        "likes": doc.get("likesCount", 0),
        "comments_count": doc.get("commentsCount", len(comments)),
        "positive_comments": pos,
        "negative_comments": neg,
        "neutral_comments": neu,
        "ownerFullName" : doc.get("ownerFullName", ""),
        "timestamp": doc.get("timestamp", ""),
        "page" : doc.get("inputUrl", "").rstrip("/").split("/")[-1]
    }
    records.append(record)
    processed_ids.add(image_name)
    counter += 1
    print(f"Processed {counter} images.")

    if counter % 10 == 0:
        df_partial = pd.DataFrame(records)
        df_partial.to_pickle(checkpoint_file)
        df_partial.to_csv("temp/fashion_progress.csv", index=False)
        print(f"Saved checkpoint at {counter} entries (pkl & csv).")

# Save final results before clustering
df = pd.DataFrame(records)
df.to_pickle(checkpoint_file)
df.to_csv("temp/fashion_progress.csv", index=False)
print("finale resuls saved (pkl & csv).")


#===========# Clustering==============
df_result = hdbscan_clustering(df)
os.makedirs("data", exist_ok=True)
df_result.to_pickle("data/fashion_with_hdbscan.pkl")
df_result.to_csv("data/fashion_clusters_hdbscan.csv", index=False)

print("Final clustering complete and data saved.")


#================ devide images into clusters
print("Dividing images into clusters...")
devide_into_clusters()
