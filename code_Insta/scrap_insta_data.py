from apify_client import ApifyClient
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

def scrap_insta_data():
    # === CONFIGURATION ===
    APIFY_TOKEN = api_key 
    MONGO_URI = "mongodb://localhost:27017/"
    MONGO_DB = "instagram_data"
    MONGO_COLLECTION = "posts"

    # === APIFY CLIENT ===
    client = ApifyClient(APIFY_TOKEN)

    # === INPUT POUR L'ACTEUR ===
    run_input = {
        "directUrls": [
            "https://www.instagram.com/whowhatwear",
            "https://www.instagram.com/ellecanada",
            "https://www.instagram.com/jacquemus",
            "https://www.instagram.com/britishvogue"
        ],
        "resultsType": "posts",
        "resultsLimit": 200,
        "searchType": "hashtag",
        "searchLimit": 1,
        "addParentData": False,
    }

    # === LANCER L’ACTEUR ===
    print("🚀 Lancement de l'acteur Instagram Scraper...")
    run = client.actor("shu8hvrXbJbY3Eb9W").call(run_input=run_input)

    # === RÉCUPÉRER LES DONNÉES ===
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    print(f"✅ {len(items)} éléments récupérés depuis Apify.")

    # === CONNEXION À MONGODB ===
    mongo_client = MongoClient(MONGO_URI)
    db = mongo_client[MONGO_DB]
    collection = db[MONGO_COLLECTION]

    # (Optionnel) Nettoyer les anciens posts de ces comptes
    usernames = [url.split("/")[-1] for url in run_input["directUrls"] if url.strip()]
    collection.delete_many({"ownerUsername": {"$in": usernames}})

    # === INSÉRER DANS MONGODB ===
    if items:
        collection.insert_many(items)
        print("💾 Données insérées avec succès dans MongoDB.")
    else:
        print("⚠️ Aucun post trouvé.")


    """pages from where data extracted
            "https://www.instagram.com/_fashion_usa1",
            "https://www.instagram.com/gucci",
            "https://www.instagram.com/zara",
            "https://www.instagram.com/vogue",
            "https://www.instagram.com/whowhatwear",
            "https://www.instagram.com/ellecanada",
            "https://www.instagram.com/jacquemus",
            "https://www.instagram.com/britishvogue"

    """
