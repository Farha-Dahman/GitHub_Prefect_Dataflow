import sys
import os
from prefect import task
from dotenv import load_dotenv

# Add the project root directory to the system path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

import logger
from database.connection import connection_db
from etl.extract_data import github_data_extraction

# Use logger
logger = logger.logger

@task
def setup():
    try:
        # Connection to the database
        connection_db("GitHub_DataStore")
        # Load environment variables from .env file
        load_dotenv()
        base_url = os.getenv("BASE_URL")
        owner = os.getenv("OWNER_NAME")
        token = os.getenv("TOKEN")
        # Request headers with authentication token
        headers = {'Authorization': f'token {token}'}
        return base_url, owner, headers
    except Exception as e:
        logger.error(f"Error during setup: {e}")
        raise

if __name__ == '__main__':
    try:
        base_url, owner, headers = setup()
        github_data_extraction(owner, headers, base_url)
    except Exception as e:
        logger.error(f"Error during execution: {e}", exc_info=True)