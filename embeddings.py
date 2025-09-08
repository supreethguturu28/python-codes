import os
import requests
import logging
from dotenv import load_dotenv
from utils import get_auth_headers

# Load environment variables from .env file
load_dotenv()

# Setup native logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def get_embeddings(text):
    try:
        embedding_service_url = os.getenv("EMBEDDING_SERVICE_API_URL")
        if not embedding_service_url:
            logger.error("EMBEDDING_SERVICE_API_URL not set in environment variables.")
            return None

        payload = {"text": text}
        response = requests.post(url=embedding_service_url, headers=get_auth_headers(), json=payload)

        if response.status_code != 200:
            logger.error(f"Error: {response.status_code}, {response.text}")
            return None
        else:
            embeddings = response.json()
            logger.info(f"Embeddings: {embeddings}")
            return embeddings

    except requests.exceptions.RequestException as e:
        logger.exception(f"Request failed: {e}")
        return None
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        return None


# Example call
if __name__ == "__main__":
    get_embeddings(text="What is CCNA?")
