import requests
import datetime
import pytz


def get_date():
    current_time = datetime.datetime.utcnow()
    est = pytz.timezone('US/Eastern')
    current_time_est = current_time.astimezone(est)
    current_date = current_time_est.strftime('%Y-%m-%d')
    return current_date


def main():
    current_date = get_date()
    earhart_xml = requests.get(f"https://api.hfs.purdue.edu/menus/v2/locations/Earhart/{current_date}")
    ford_xml = requests.get(f"https://api.hfs.purdue.edu/menus/v2/locations/Ford/{current_date}")
    hillenbrand_xml = requests.get(f"https://api.hfs.purdue.edu/menus/v2/locations/Hillenbrand/{current_date}")
    wiley_xml = requests.get(f"https://api.hfs.purdue.edu/menus/v2/locations/Wiley/{current_date}")
    windsor_xml = requests.get(f"https://api.hfs.purdue.edu/menus/v2/locations/Windsor/{current_date}")

    xml_content = windsor_xml.content.decode('utf-8')
    print(xml_content)


if __name__ == "__main__":
    main()
