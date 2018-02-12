"""
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
"""
import csv
import re
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'


def write_file(output_file, header, data):
    with open(output_file, 'w') as w:
        writer = csv.DictWriter(w, delimiter=',', fieldnames=header)
        writer.writeheader()

        for datum in data:
            writer.writerow(datum)
    w.close()


def process_file(input_file, output_good, output_bad):

    good_data = []
    bad_data = []
    header = 'NULL'

    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames

        for datum in reader:

            """
            returns the lowest index in string
            if row['URI'].find('dbpedia.org) < 0:
            """

            """
            Alternative way to avoid continue

            for row in reader:
            # validate URI value
            if row['URI'].find("dbpedia.org") < 0:
                continue

            ps_year = row['productionStartYear'][:4]
            try: # use try/except to filter valid items
                ps_year = int(ps_year)
                row['productionStartYear'] = ps_year
                if (ps_year >= 1886) and (ps_year <= 2014):
                    data_good.append(row)
                else:
                    data_bad.append(row)
            except ValueError: # non-numeric strings caught by exception
                if ps_year == 'NULL':
                    data_bad.append(row)
            """


            if re.search('dbpedia.org', datum['URI']) is None:
                continue

            year = datum['productionStartYear']
            if year != 'NULL':

                """
                scope[0:4] = [:4]
                """
                year_digits = int(re.sub(r'\D', '', year)[0:4])
                if year_digits >= 1886 and year_digits <= 2014:
                    datum['productionStartYear'] = year_digits
                    good_data.append(datum)
                    continue
            bad_data.append(datum)
        f.close()

    write_file(output_good, header, good_data)
    write_file(output_bad, header, bad_data)


def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()