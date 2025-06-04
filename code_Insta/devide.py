import os
import pandas as pd
import shutil


def devide_into_clusters():
    # === Paths ===
    CSV_PATH = "data/fashion_clusters_powerbi.csv"
    ORIGINAL_IMAGES_DIR = "images/original_images"
    CLUSTERED_DIR = "images/clustered_by_model"

    # === Load CSV ===
    df = pd.read_csv(CSV_PATH)

    # === Create folders for each cluster ===
    for cluster_id in df['cluster'].unique():
        cluster_path = os.path.join(CLUSTERED_DIR, str(cluster_id))
        os.makedirs(cluster_path, exist_ok=True)

    # === Move images to their corresponding cluster folder ===
    for _, row in df.iterrows():
        shortcode = row['shortCode']  # or 'filename' if you have filename instead
        cluster = row['cluster']
        
        src = os.path.join(ORIGINAL_IMAGES_DIR, f"{shortcode}.jpg")
        dst = os.path.join(CLUSTERED_DIR, str(cluster), f"{shortcode}.jpg")

        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"✅ Moved: {shortcode}.jpg → Cluster {cluster}")
        else:
            print(f"❌ Image not found: {src}")
