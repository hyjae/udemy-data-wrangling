Data Cleaning
=====
Data cleaning is an iterative process to find missing data, outlier, different formats(date).


### Strategy
- Validity
    - date: unnecessary chars, range, format check
    - Separate them into two files; good, bad output for later use  
    - Useful module: **re.sub()**
    - [validity.py](https://github.com/yjhnnn/DataWrangling/blob/master/DataCleaning/validity.py)
- Multiple Data
    - ex) names, addresses, nationalities and so on
    - Putting them in a dictionary with a list of values
    - [name.py](https://github.com/yjhnnn/DataWrangling/blob/master/DataCleaning/name.py)
- Auditing
    - Store the possible types of each col as a set in a dictionary
    - Useful function: **set** to prevent dulicates
    - Determining one value using the most sig digits
    - [audit.py](https://github.com/yjhnnn/DataWrangling/blob/master/DataCleaning/audit.py)

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

**Note: If a cell contains two values and need to choose one,
choose the one with the most significant digits**

