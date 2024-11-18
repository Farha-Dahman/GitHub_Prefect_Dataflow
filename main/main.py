import sys
import os
import logging
from prefect import task
from dotenv import load_dotenv

# Add the project root directory to the system path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

from database.connection import connection_db
from etl.extract_data import github_data_extraction

logger = logging.getLogger(__name__)

@task
def setup():
    try:
        logger.info("Setting up...")
        # Connection to the database
        connection_db("GitHub_DataStore")
        # Load environment variables from .env file
        load_dotenv()
        base_url = os.getenv("BASE_URL")
        owner = os.getenv("OWNER_NAME")
        token = os.getenv("TOKEN")
        # Request headers with authentication token
        headers = {'Authorization': f'token {token}'}
        logger.info("Setup completed successfully.")
        return base_url, owner, headers
    except Exception as e:
        logger.error(f"Error during setup: {e}")
        raise

if __name__ == '__main__':
    try:
        base_url, owner, headers = setup()
        logger.info("Starting data extraction...")
        github_data_extraction(owner, headers, base_url)
        logger.info("Data extraction completed.")
    except Exception as e:
        logger.error(f"Error during execution: {e}", exc_info=True)
