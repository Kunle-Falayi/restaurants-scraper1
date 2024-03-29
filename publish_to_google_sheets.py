import gspread
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
import os
import json

def publish_to_google_sheets():
    # Load the Google service account key from environment variable
    creds_json = os.getenv('GOOGLE_SERVICE_ACCOUNT_KEY')
    print("Loaded JSON:", creds_json)


    # Print out the loaded JSON (for debugging)
    print("Loaded JSON:", creds_json)

    # Attempt to load the JSON into a dictionary
    try:
        # Remove newlines and load JSON
        creds_dict = json.loads(creds_json.replace('\n', ''))
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return

    # Create a Google Credentials object
    creds = Credentials.from_service_account_info(creds_dict)

    # Authorize the client
    client = gspread.authorize(creds)

    # Open the Google Sheets document by its title
    sheet = client.open('Restaurant_inspection_database(auto_scraper)').sheet1

    # Example: Write data to a specific cell
    sheet.update('A1', 'Hello, Google Sheets!')

if __name__ == "__main__":
    publish_to_google_sheets()
