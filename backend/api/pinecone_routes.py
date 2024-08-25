from flask import Blueprint, request, jsonify
from service.pinecone_service import insert_vector, query_vectors

api = Blueprint('api', __name__)

@api.route('/insert', methods = ['POST'])
def insert():
    feature_vector = []
    insert_vector(userid, feature_vector)
    return jsonify({"status":"success"}), 200


@api.route('/query', method = ['POST'])
def query():
    feature_vector = []
    results = query_vectors(feature_vector, 10)
    return jsonify(results), 200