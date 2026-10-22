
import qdrant_client
from dotenv import load_dotenv
import os

load_dotenv()

client = qdrant_client.QdrantClient(url=os.getenv('QDRANT_URL'), api_key=os.getenv('QDRANT_API_KEY'))

print(client.get_collections())