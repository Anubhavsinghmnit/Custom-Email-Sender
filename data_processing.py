# data_processing.py
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

def load_data(file_path=None, google_sheet_id=None, google_api_credentials=None):
    """
    Loads data from a CSV file or Google Sheets.
    
    Args:
        file_path (str): Path to the CSV file.
        google_sheet_id (str): Google Sheet ID if loading from Google Sheets.
        google_api_credentials (str): Path to the JSON credentials file for Google Sheets API.
    
    Returns:
        DataFrame: Loaded data as a pandas DataFrame.
    """
    if file_path:
        # Load data from a CSV file
        data = pd.read_csv(file_path)
    elif google_sheet_id and google_api_credentials:
        # Load data from Google Sheets
        credentials = service_account.Credentials.from_service_account_file(
            google_api_credentials,
            scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]
        )
        service = build("sheets", "v4", credentials=credentials)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=google_sheet_id, range="Sheet1").execute()
        values = result.get("values", [])
        
        # Convert Google Sheets data to a DataFrame
        data = pd.DataFrame(values[1:], columns=values[0])
    else:
        raise ValueError("Provide either a CSV file path or Google Sheets ID and credentials.")
    
    return data

def detect_columns(data):
    """
    Detects columns in the provided data.
    
    Args:
        data (DataFrame): Loaded data as a pandas DataFrame.
    
    Returns:
        list: List of column names in the data.
    """
    return data.columns.tolist()
