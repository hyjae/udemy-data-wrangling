Data Extraction
======
Basic extraction method based on the types of files.  
**Summary**
1. Tabular - csv.DictReader
2. XLRD
3. JSON 
4. XML - xml.etree.ElementTree

Tabular
------

- CSV format
- Fields are separated by delimeter(,); TSV(tab)
- The first line is always column names
- Prone to error due to the extra ',' or others
- Using csv.DictReader
to avoid this problem  
ex) [beatles_csv.py](https://github.com/yjhnnn/DataWrangling/DataExtraction/beatles_csv.py)

XLRD
------
- It is designed to work with excel files

JSON
------
- Items may have different field
- May have nested objects
- Using requests to extract json data

#### reguests
```angular2html
# passing parameters
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get('http://httpbin.org/get', params=payload)
>>> print(r.url)
http://httpbin.org/get?key2=value2&key1=value1
```  
[Official Documentations](http://docs.python-requests.org/en/master/user/quickstart/#make-a-request)

#### Using API
   - Understand the structure of API given
   - Using requests module to get json data  
   - Using dumps function to print out 
   - Using codecs module to write unicode files
   - Using authentication with web APIs  
   ex) [nytimes_json.py](https://github.com/yjhnnn/DataWrangling/DataExtraction/nytimes_json.py)

XML
------
- It is designed to transfer data efficiently between
consumer product and producer product
- Easy to write code to read/write
- Robust parcers in most languages
- Easy to change the format to ex)html, pdf etc
- Document oriented vs Data oriented

#### Parsing XML
```python
import xml.etree.ElementTree as ET
```
- .tag: see the all nested tags
- .find: find a single tag
- .text: returns text
