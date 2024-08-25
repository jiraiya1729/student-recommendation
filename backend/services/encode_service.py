from models.encoder import embedding_model
import numpy as np


def encode_features(story, major, hobbies, country, unique_quality):
    
    story_embedding = embedding_model.encode(story)
    major_embedding = embedding_model.encode(major)
    hobbies_embedding = embedding_model.encode(hobbies)
    country_embedding = embedding_model.encode(country)
    unique_quality_embedding = embedding_model.encode(unique_quality)
    
    features = np.concatenate([
        story_embedding,
        major_embedding,
        hobbies_embedding,
        country_embedding,
        unique_quality_embedding
    ])

    return features
