import pinecone
from core.config import Config

def create_client():
    pinecone.init(api_key = Config.PINECONE_API_KEY)
    index_name = "student_recommendation"
    return pinecone.Index(index_name)