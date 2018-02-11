"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above,
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import re
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def check_url(url):
    match = re.search('dbpedia.org', url)
    if match is not None:
        return True
    return False


def get_year(productionStartYear):
    return re.sub(r"\D", "", productionStartYear)[0:4]


def check_year(productionStartYear):

    if productionStartYear == 'NULL':
        return False

    date = get_year(productionStartYear)
    if int(date) < 1886 or int(date) > 2014:
        return False
    return True


def write_file(output, index, reader, years):

    header = reader.fieldnames

    with open(output, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames=header)
        writer.writeheader()
        for i, row in enumerate(reader, -1):
            if i in index:
                #row['producntionStartyear'] = years[i]
                writer.writerow(row)
    g.close()


def process_file(input_file, output_good, output_bad):

    good_indexes = []
    bad_indexes = []
    years = []

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        for da in reader:
            print(da)

        # Note: reader starts from the second line of csv file assigning
        # the first line as a header. Second line corresponds the index of 0
        for i, datum in enumerate(reader):
            #years.append(check_year(datum['productionStartyear']))
            if check_url(datum['URI']) is False:
                continue
            if check_year(datum['productionStartYear']) is True:
                good_indexes.append(i)
            else:
                bad_indexes.append(i)

        f.seek(0)
        write_file(output_good, good_indexes, reader, years)
        f.seek(0)
        write_file(output_bad, bad_indexes, reader, years)
        f.close()


def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()