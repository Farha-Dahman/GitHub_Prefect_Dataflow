def store_data_in_database(data, model):
    """
    Store the fetched data into the MongoDB database using the provided model.
    """
    try:
        # Iterate through the data and save each item to the database
        for item in data:
            # Attempt to save the item to the database
            try:
                model(**item).save()
            except Exception as e:
                # Handle any exceptions that occur during the saving process
                print(f"Error saving item to database: {e}")
    except Exception as e:
        # Handle any exceptions that occur during the iteration process
        print(f"Error iterating through data: {e}")
