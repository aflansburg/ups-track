from bs4 import BeautifulSoup
import urllib.request
import re
import pprint

pp = pprint.PrettyPrinter(indent=4)
statuses = {}

with open("ups.txt", 'r') as f_in:

    TrackingNumbers = filter(None, (line.rstrip() for line in f_in))

    for trcknum in TrackingNumbers:
        track_table = []
        response = urllib.request.urlopen("https://wwwapps.ups.com/WebTracking/track?track=yes&trackNums=" + trcknum + "&loc=en_us")
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.find('table', {'class': 'dataTable'}).findAll('tr')
        for row in rows:
            cols = [re.sub('\s+', ' ', ele.text.strip()).encode('ascii', 'ignore') for ele in row.findAll('td')]
            if cols:
                track_table.append([ele for ele in cols])

        date = track_table[0][1].decode("utf-8")
        status = track_table[0][3].decode("utf-8")
        statuses.update({
            trcknum: {
                'status_date': date,
                'status': status
            }
        })

pp.pprint(statuses)
