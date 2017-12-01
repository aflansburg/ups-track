import csv
import re
import urllib.request
from bs4 import BeautifulSoup


def get_statuses(file):
    with open(file) as f_in:
        statuses = []
        tracking_numbers = filter(None, (line.rstrip() for line in f_in))

        for track_no in tracking_numbers:
            track_table = []

            html = get_source(track_no)
            rows = parse_source(html)

            track_table.append(strip_info(rows))

            statuses.append(
                build_data_dict(track_table, track_no)
            )
        f_in.close()
        return statuses


def write_to_file(status_dict):
    print(status_dict)
    out_file = 'ups_track_status.csv'
    col_names = ['trk_no', 'status_date', 'status']

    with open(out_file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=col_names)
        writer.writeheader()
        writer.writerows(status_dict)

    csv_file.close()


def get_source(tracking):
    base_url = "https://wwwapps.ups.com/WebTracking/track?track=yes&trackNums="
    locale_key = "&loc=en_us"
    response = urllib.request.urlopen(base_url + tracking + locale_key)
    html = response.read()
    return html


def parse_source(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find('table', {'class': 'dataTable'}).findAll('tr')
    return data


def strip_info(table_data):
    for row in table_data:
        cols = [re.sub('\s+', ' ', ele.text.strip()).encode('ascii', 'ignore') for ele in row.findAll('td')]
        if len(cols) > 0:
            return cols


def build_data_dict(data, trcknum):
    date = data[0][1].decode("utf-8")
    status = data[0][3].decode("utf-8")
    temp_dict = {
        'trk_no': trcknum,
        'status_date': date,
        'status': status
    }
    return temp_dict
