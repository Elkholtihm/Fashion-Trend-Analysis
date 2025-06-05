# Fashion Trends Analysis Project

This project is a comprehensive system for analyzing fashion trends by processing multimodal data (text, images, and numerical metrics) from Instagram and eBay. It leverages advanced machine learning techniques to scrape, process, and visualize data, providing insights into consumer preferences, emerging trends, and market dynamics. The pipeline includes data ingestion, image and text processing, sentiment analysis, clustering, and interactive dashboards for actionable insights.

---

## Technologies Used

### Programming & Libraries
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)  
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)  
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)  
[![Requests](https://img.shields.io/badge/Requests-005571?style=for-the-badge)](https://docs.python-requests.org/)  
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)  
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)  
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)


### Data Storage
[![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)


### Web Scraping
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4B0082?style=for-the-badge)](https://www.crummy.com/software/BeautifulSoup/)  
[![Scrapy](https://img.shields.io/badge/Scrapy-2E8B57?style=for-the-badge&logo=scrapy&logoColor=white)](https://scrapy.org/)  
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)


### Computer Vision & Deep Learning
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)  
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)  
[![YOLOv8](https://img.shields.io/badge/YOLOv8-000000?style=for-the-badge&logo=ultralytics&logoColor=white)](https://docs.ultralytics.com/)  
[![Segment Anything](https://img.shields.io/badge/Segment_Anything-000000?style=for-the-badge)](https://github.com/facebookresearch/segment-anything)


### NLP Models
[![BERT](https://img.shields.io/badge/BERT-0052CC?style=for-the-badge)](https://huggingface.co/transformers/model_doc/bert.html)  
[![Sentence-BERT](https://img.shields.io/badge/Sentence--BERT-0052CC?style=for-the-badge)](https://www.sbert.net/)  
[![Transformers](https://img.shields.io/badge/Transformers-HuggingFace-ffcc00?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/transformers/)  
[![sentence-transformers](https://img.shields.io/badge/sentence--transformers-FFB300?style=for-the-badge)](https://github.com/UKPLab/sentence-transformers)


### Machine Learning Algorithms
[![Random Forest](https://img.shields.io/badge/Random_Forest-007ACC?style=for-the-badge)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)  
[![HDBSCAN](https://img.shields.io/badge/HDBSCAN-8A2BE2?style=for-the-badge)](https://hdbscan.readthedocs.io/en/latest/)


### Data Visualization
[![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)

## 🏗️ Architecture

![System Architecture](./architecture.png)

## 📁 Project Structure

The project is organized into three main components:

- **Instagram Data Pipeline (`code_Scrap_process_Instagram_data`)**:  
  Scrapes Instagram data, processes images and text, performs segmentation, sentiment analysis, and model training.

- **eBay Fashion Data Pipeline (`code_Scrap_process_Ebay_data`)**:  
  Collects and processes eBay fashion product data, including descriptions, prices, and feedback.

- **Dashboards**:  
  Interactive Power BI dashboards for visualizing trends, engagement metrics, and sentiment analysis for both Instagram and eBay data.

---

## Folder Structure

```
code_Scrap_process_Instagram_data/
├── code_Insta/
├── data/
├── devide.py
├── download_images.py
├── encode_image.py
├── HDBSCAN_clusters.py
├── images/
├── model_train/
├── models/
├── run.py
├── scrap_insta_data.py
├── segment-anything/
├── segment.py
├── sentiment_analysis.py
├── temp/
├── myenv/
├── Readme
├── requirements.txt
```

## System Architecture

The system is designed to process multimodal data through a pipeline of ingestion, storage, processing, and visualization.

---

## Prerequisites

- Python 3.11.8
- MongoDB for data storage
- Power BI for dashboard visualization
- Required Python libraries (listed in `requirements.txt`)

---

## Setup Instructions

### 1. Download Project Files
Download the full project from this [Google Drive link](https://drive.google.com/drive/folders/17iqyuFY5RwhNZDRW5BseI3-Zm0J75Kz5) due to the large size of some files (e.g., datasets, trained models).

### 2. Navigate to the Segment Anything Model

```bash
cd code_Scrap_process_Instagram_data/segment-anything
```

### 3. Install Segment Anything

```bash
pip install -e .
```

### 4. Install Dependencies

Ensure Python is installed, then run:

```bash
pip install -r requirements.txt
```

### 5. Set Up MongoDB

- Install MongoDB locally or use a cloud instance.
- Configure the connection in scripts like `scrap_insta_data.py` or eBay scripts.

### 6. Run the Instagram Data Pipeline

```bash
cd code_Scrap_process_Instagram_data/
python run.py
```

This script orchestrates:

- Scraping: `scrap_insta_data.py`
- Image downloading: `download_images.py`
- Encoding: `encode_image.py`
- Segmentation: `segment.py`
- Clustering: `HDBSCAN_clusters.py`
- Sentiment Analysis: `sentiment_analysis.py`

### 7. Run the eBay Data Pipeline

Refer to readme file in code_Scrap_process_Ebay_data

---

## Launch Dashboards

- Open Power BI dashboard files in the `Dashboards/` folder using Power BI Desktop.

---

## Key Components

### Instagram Pipeline

- **Scraping**: Collects images, captions, and comments (`scrap_insta_data.py`)
- **Image Processing**: Downloads (`download_images.py`), encodes (`encode_image.py`), and segments (`segment.py`)
- **Clustering**: Groups similar posts using HDBSCAN (`HDBSCAN_clusters.py`)
- **Sentiment Analysis**: Uses BERT-based models (`sentiment_analysis.py`)

### Dashboards

- **Instagram**: Engagement metrics, sentiment distribution, cluster visualization
- **eBay**: Product volumes, pricing trends, color preferences, and feedback

---

## Perspectives (Future Work)

To enhance the system further, we plan to:

- **Develop a Web-Based Dashboard using Django**  
  Replace Power BI with a fully interactive web dashboard built using Django for real-time monitoring and visualization.

- **Enable Automated and Batch Updates**  
  Implement periodic scraping and processing tasks using Celery and Django Background Tasks to ensure data freshness without manual execution.

- **Use a Data Warehouse instead of CSV files**  
  Integrate a proper data warehousing solution such as Google BigQuery, Amazon Redshift, or PostgreSQL for efficient large-scale querying, replacing local CSV-based analytics.

---

## Acknowledgments

This project was inspired by the [Future Fashion Trends Forecasting](https://github.com/surabhi135/Future-Fashion-Trend-Forecasting) repository.

Special thanks to **Professor Imad Sassi** for his invaluable guidance and support throughout the project.
