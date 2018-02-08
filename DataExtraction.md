## Data Extraction
Tabular
------

- CSV format
- Fields are separated by delimeter(,); TSV(tab)
- The first line is always column names
- Prone to error due to the extra ',' or others
    - Use csv module to avoid this problem


XLRD
------
- It is designed to work with excel files

JSON
------
- Items may have different field
- May have nested objects

#### Reguests
[Documentation](http://docs.python-requests.org/en/master/user/quickstart/#make-a-request)
```angular2html
# passing parameters
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get('http://httpbin.org/get', params=payload)
>>> print(r.url)
http://httpbin.org/get?key2=value2&key1=value1
```

XML
------
- It is designed to transfer data efficiently between
consumer product and producer product
- Easy to write code to read/write
- Robust parcers in most languages
- Easy to change the format to ex)html, pdf etc
- Document oriented vs Data oriented

#### Parsing XML
