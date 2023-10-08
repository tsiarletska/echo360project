from datetime import datetime, timedelta
from requests import Session
import json
import csv
import time

# access token
session = Session()

# Getting the access token
def access_token_function(): 
    headers = {
    "Accepts": "application/json",}

    session = Session()
    session.headers.update(headers)


    token_url = "https://echo360.org.uk:443/oauth2/access_token"
    token_parameters = {
        "grant_type": "xxxxx",
        "client_id": "xxxxx",
        "client_secret": "xxxxx"}
    token_responce = session.post(token_url, params=token_parameters)
    token_data = json.loads(token_responce.text)
    access_token = token_data["access_token"]
    return access_token


access_token = access_token_function()
print("Access Token:", access_token)


# ALL POSSIBLE REPORTS (REPORTS NAMES)
# asset
# assetbydate
# presentation
# videoview
# confused
# pollingv2
# qandav2
# notes
# viewsessions
# viewsessiondetails
# liveviews

needed_report_name = input("Write the name of the needed report:")

# ... (previous code)

def report_dates(start_date):
    end_date = start_date + timedelta(days=6)
    request_report_url = ("https://echo360.org.uk:443/public/api/v1/reporting/requests/" + needed_report_name)
    request_report_parameters = {
        "access_token": access_token,
        "reportName": needed_report_name,
        "parameters": {
            "start": start_date.strftime("%Y-%m-%d"),  # Convert to string
            "end": end_date.strftime("%Y-%m-%d"),  # Convert to string
        },
        "output": {
            "output": "json",
            "compression": False,
            "delimiter": ",",
        },
    }

    headers = {
        "Content-Type": "application/json"}
    request_report_responce = session.post(request_report_url, headers=headers, json=request_report_parameters)

    print(request_report_responce.text)

    response_data = request_report_responce.json()
    request_id = response_data.get('requestId')
    print(f'REQUEST_ID: {request_id}')
    print(f'start date: {start_date.strftime("%Y-%m-%d")}, end date: {end_date.strftime("%Y-%m-%d")}')
    print(request_id)


    # print(f"The best week ever! From {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")

while True:
    date_str = input("Write a date (YYYY-MM-DD): ")
    date_format = "%Y-%m-%d"
    try:
        given_date = datetime.strptime(date_str, date_format)
        break  # Exit the loop if a valid date is provided
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.")

for _ in range(3):
    report_dates(given_date)
    given_date += timedelta(weeks=1)