# ups-track

#### Fork of callum-ryan/ups-track

##### In this fork:

* Updated to Python 3.6.3
* Added urllib.request
* Results returned as dictionary and only for Delivery Status and Status Date, however this
this can be easily altered to suit your own requirements

ups-track simply uses urllib.request and BeautifulSoup4 to scrape the
UPS tracking page for the shipping progress/status data table.

It is not incredibly fast for obvious reasons, but it does work and it is
simple.

The output path is currently ```output/ups_track_status.csv``` so this may
need to be altered to match your directory structure.