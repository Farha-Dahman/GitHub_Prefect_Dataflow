import os
from dotenv import load_dotenv
from mongoengine import connect

def connection_db(db_name):
    """
    Function to establish connection to MongoDB using the connection string from environment variables.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Get the MongoDB connection string from environment variables
    uri = os.getenv("CONNECTION_STRING")

    # Establish the mongoengine connection
    connect(host=uri, db=db_name)