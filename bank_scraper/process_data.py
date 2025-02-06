import json
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
import uuid
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

if not PINECONE_API_KEY:
    raise ValueError("Pinecone API Key not found. Set it in .env file.")

# Load stored scraped data (e.g., from a JSON file)
with open("output.json", "r", encoding="utf-8") as f:
    scraped_data = json.load(f)

# Initialize embedding model and Pinecone
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Initialize Pinecone client
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = "banking-index"
if index_name not in pc.list_indexes().names():
    from pinecone import ServerlessSpec
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1" 
        )
    )

# Connect to the index
index = pc.Index(index_name)


# Process and store data
try:
    # Process and store data
    for item in scraped_data:
        if "chunks" in item:
            for chunk in item["chunks"]:
                embedding = model.encode(chunk).tolist()  # Convert embedding to list
                try:
                    # Add relevant metadata, including the content of the chunk
                    metadata = {
                        "url": item["url"],
                        "type": item["type"],
                        "content": chunk  # Store the actual content (chunk text)
                    }
                    # Upsert data into Pinecone
                    index.upsert([(str(uuid.uuid4()), embedding, metadata)])
                except Exception as e:
                    print(f"Error upserting data for chunk: {chunk}. Error: {e}")
    print("Data successfully stored in Pinecone!")
except Exception as e:
    print(f"Error processing the data: {e}")



