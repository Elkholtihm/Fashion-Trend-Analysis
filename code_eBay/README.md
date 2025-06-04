🛍️ Fashion Trend Analysis Pipeline
This repository provides a modular pipeline for collecting, cleaning, and analyzing fashion-related data, including AI-based categorization and sentiment analysis.

📁 Project Structure
.
├── app/
├── data/
├── models/
├── src/
├── notebooks/
├── main/

🔹 app/
Currently empty. Intended to hold the core application logic or web interface in the future.

🔹 data/
Contains both raw and processed datasets. Processed data files are versioned for reproducibility.

Structure:

data/
├── raw/
├── processed_v1/
├── processed_v2/
🔹 models/
Includes AI components such as classifiers and analyzers used in the pipeline.

Files:

categorize.py: Classifies products based on category.

sentiment_analyser.py: Analyzes user sentiment from reviews or comments.

🔹 src/
Contains utility scripts and data preprocessing modules.

Files:

cleaner.py: Cleans and standardizes textual and numerical fields.

ebay_cloths.py: Extracts and processes fashion-specific attributes from eBay product listings.

🔹 notebooks/
Jupyter notebooks used to prototype, collect data, and apply the processing pipeline interactively.

Files:

product_scraper.ipynb: Collects fashion data from online sources.

cleaning.ipynb: Applies cleaning functions from src/.

data_enhancement.ipynb: Enriches data with additional metadata or features.

apply_ai_models.ipynb: Runs AI models from models/ for analysis and insight extraction.

🔹 main/
Contains the core automation scripts that orchestrate storage and processing.

Files:

insert_data.py: Handles data insertion into the storage system (e.g., database).

processing.py: Coordinates the full pipeline from raw data to final, cleaned datasets.

>>this folder should be used to automate the whole process as the futur perspectve

🧠 Purpose
This structure supports scalable experimentation and development in the field of fashion data analysis, combining data engineering, AI models, and exploratory analysis in one organized pipeline.