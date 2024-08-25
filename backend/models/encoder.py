from sentence_transformers import sentence_transformers
from core.config import Config


embedding_model = sentence_transformers(Config.EMBEDDING_MODEL_NAME)