from encode import encode_features
from flask_cors import CORS
from recommend import recommend
from flask import Flask, request, jsonify


app = Flask(__name__)

CORS(app)
# CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/recommend', methods=['POST'])
def recommend_users():
    data = request.json
    
    print(data) 
    features = encode_features(data['story'], data['major'], data['hobbies'], data['country'], data['unique_quality'])
    print(features.shape)
    userids = recommend(features)
    return jsonify({"status": "success", "message": "Data received", "recommendations": userids }), 200

if __name__ == '__main__':
    app.run(debug=True)
