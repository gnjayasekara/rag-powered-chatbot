from pinecone_utils import query_pinecone
from response_generator import generate_response

# Example query
query = "What are the current interest rates for 3 months fixed deposits in commercial bank?"

# Step 1: Query Pinecone for relevant chunks
relevant_chunks = query_pinecone(query)

# Step 2: Generate response using those chunks
response = generate_response(query, relevant_chunks)

# Print the response
print(response)
