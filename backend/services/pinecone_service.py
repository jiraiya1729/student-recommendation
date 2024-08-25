from models.pinecone_client import index

def insert_vector(userid, vector):
    index.upsert(vectors = [str(userid), vector])
    
    
def query_vector(vector, top_k):
    result = index.query(vector, top_k)
    return result['macthes']