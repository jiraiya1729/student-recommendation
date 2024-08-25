from flask import Blueprint, request, jsonify
from services.encoding_service import encode_features

api = Blueprint('api', __name__)

@api.route('/encode', methods = ['POST'])
def encode():
    
    features = encode_features(story, major, hobbies, country, unique_quality)
    return jsonify({"vectors": features.tolist()}), 200


