from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key = '')

index = pc.Index('')

def recommend(features):
    result = index.query(
        vector = features.tolist(),
        top_k = 10
    )
    print(result)
    userids = [match['id'] for match in result['matches']]
    return userids