from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key = 'c2e5f0ee-76a2-4130-87b2-3caf15a2942c')

index = pc.Index('student-recommendations')

def recommend(features):
    result = index.query(
        vector = features.tolist(),
        top_k = 10
    )
    print(result)
    userids = [match['id'] for match in result['matches']]
    return userids