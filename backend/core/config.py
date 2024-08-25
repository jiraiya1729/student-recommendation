import os 

class Config:
    PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
    EMBEDDING_MODEL_NAME = 'paraphrase-MiniLM-L6-v2'