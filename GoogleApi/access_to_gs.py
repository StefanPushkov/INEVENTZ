import gspread
from oauth2client.service_account import ServiceAccountCredentials


# result = first.row_values(6)
# print(first.get_all_records())
def append_data_to_gsheets(time_stamp: int, normal_time: str, username: str, text: str, link_to_post: str):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('E:\INEVENTZ\GoogleApi\semanticnew-266420-416936ff312e.json', scope)
    client = gspread.authorize(creds)

    gspreadsheets = client.open('DataBase_SemanticNew')

    first = gspreadsheets.get_worksheet(0)

    first.append_row([time_stamp, normal_time, username, text, link_to_post])