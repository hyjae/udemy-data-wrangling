Screen Scraping
=====

HTML
-----
- Build list of values you need(Grab)
- Make HTTP request to download all data
- Parse the data file

#### Developer Tool
- Form Data: It tells the number of parameters needed to pass as a part of requrests
- For the most cases, there are hidden form requests

#### BeautifulSoup
- Parse the html trees; similar to XML parsing tree

#### Best Pratice for Scraping
- Look at how a browser makes requests using developer tools
- Emulate in code
- If it breaks up, look at your http traffic  
ex) [carrier_html.py](https://github.com/yjhnnn/DataWrangling/ScreenScraping/carrier_html.py),
[extract_html.py](https://github.com/yjhnnn/DataWrangling/ScreenScraping/extract_html.py)
