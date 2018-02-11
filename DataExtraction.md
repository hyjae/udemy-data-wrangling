Data Extraction
======
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
- .tag: see the all nested tags
- .find: find a single tag
- .text: returns text

Data Wrangling Procedure
-----
#### HTML
- Build list of values you need(Grab)
- Make HTTP request to download all data
- Parse the data file

#### Developer Tool
- Form Data: It tells the number of parameters needed to pass as a part of requrests
- For the most cases, there are hidden form requests

#### BeautifulSoup
- Parse the html trees; similar to XML parsing tree

#### Best Pratice for Scraping
- Look at how a browser makes requests(developer tools)
- Emulate in code
- If it breaks up, look at your http traffic

Data Cleaning
=====
- Data cleaning is an iterative process
- Missing, outlier, different formats(date), etc

### Sources of Dirty Data
- User entry errors
- Different schemas
- Legacy systems
- Evolving applications
- Lost from data migration
- No unique identifiers
- Programmer errors
- Corruption in transmission

### Measures of Data Quality
- Validity: Conforms to a schema 
- Accuracy: Conforms to gold standard
    - ex) Trusted addresses to verify the addresses in source
- Completeness: All records?
- Consistency: Match fields across systems
- Uniformity: Same units

### Clearning Procedure
- Audit your data using validation tools
- Auditing validity
    - unique value
    - mandatory value
    - foreign-key constraints
    - certain range, format(size, date etc)
    
- Create a data cleaning plan
    - Identify causes
    - Define operations
    - Test
- Execute plan(running a script)
- Manually correct

### Auditing a Cross-Field Constraint
- Multiple fields per item

