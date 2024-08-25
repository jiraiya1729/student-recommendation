from flask import Flask
from api.pinecone_routes import api as pinecone_api
from api.encoding_routes import api as encoding_api

app = Flask(__name__)

app.register_blueprint(pinecone_api, url_prefix = '/api/pinecone' )
app.register_blueprint(encoding_api, url_prefix = '/api/encoding')

if __name__ == '__main__':
    app.run(debug = True)