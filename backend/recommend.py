from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

api_key = os.getenv('PINECONE_API_KEY')
pc = Pinecone(api_key = api_key)

index = pc.Index('')

def recommend(features):
    result = index.query(
        vector = features.tolist(),
        top_k = 10
    )
    print(result)
    userids = [match['id'] for match in result['matches']]
    return userids


def insert_user_features(userid, features):
    index.upsert(vectors = [(str(userid), features.tolist())])
    return
    
