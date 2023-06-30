import requests
import datetime
import pytz
import pyodbc
import json

connection_string = f""
table_name = ''


def get_date():
    current_time = datetime.datetime.utcnow()
    est = pytz.timezone('US/Eastern')
    current_time_est = current_time.astimezone(est)
    current_date = current_time_est.strftime('%Y-%m-%d')
    return current_date


def format_json(name, date):
    req_info = requests.get(f"https://api.hfs.purdue.edu/menus/v2/locations/{name}/{date}")
    json_content = req_info.json()
    print(json_content)
    json_dump = json.dumps(json_content)
    return json_dump


def main():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Clear all entries from the table
    delete_all_query = f'DELETE FROM {table_name}'
    cursor.execute(delete_all_query)

    current_date = get_date()

    dining_courts = ["Earhart", "Ford", "Hillenbrand", "Wiley", "Windsor"]

    for dining_court in dining_courts:
        json_string = format_json(dining_court, current_date)

        # Load and Insert the JSON data into the table
        data = json.loads(json_string)
        meals = data['Meals']

        if len(meals) == 0:
            continue

        rows_to_insert = [
            (data['Date'], data['Location'], meal['Name'], item['Name'])
            for meal in meals
            for station in meal['Stations']
            for item in station['Items']
        ]

        found_item = len(rows_to_insert) > 0

        # Perform batch insert
        if found_item:  # ensures there is data
            insert_query = f"INSERT INTO {table_name} (Date, Location, Type, Name) VALUES (?, ?, ?, ?)"
            cursor.executemany(insert_query, rows_to_insert)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
