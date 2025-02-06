from pinecone import Pinecone
import os
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv


load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

if not PINECONE_API_KEY:
    raise ValueError("Pinecone API Key not found. Set it in .env file.")

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



model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to query Pinecone index
def query_pinecone(query: str, top_k: int = 5):
    """
    Query the Pinecone vector database for the most similar chunks to the input query.

    Args:
        query (str): The user query.
        top_k (int): The number of top matches to retrieve from Pinecone.

    Returns:
        List of dictionaries containing score and metadata (text).
    """
    # Encode the query into a vector
    query_vector = model.encode(query)

    # Convert ndarray to a list for Pinecone serialization
    query_vector = query_vector.tolist()

    # Query Pinecone for the top_k most similar results
    results = index.query(vector=query_vector, top_k=top_k, include_metadata=True)

    # Output the results (you can also return this for later use)
    matched_chunks = []
    for match in results["matches"]:
        matched_chunks.append({
            "score": match['score'],
            "data": match['metadata']
        })
        # Print individual match details
        print(f"Score: {match['score']}, Data: {match['metadata']}")

    return matched_chunks

# # Example query to test
# query = "What are the current interest rates for fixed deposits?"
# results = query_pinecone(query)

# # Printing the returned results
# for result in results:
#     print(result)
