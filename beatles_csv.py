import csv


DATADIR = ""
DATAFILE = "beatles-diskography.csv"

def parse_file(datafile):
    dictlist = []
    with open(datafile, "r") as f:
        colnames = []
        firstline = f.readline()
        for col in firstline.split(','):
            colnames.append(col.strip('\n'))
        for i, line in enumerate(f):
            if i == 10:
                break
            else:
                data = [word.strip('\n') for word in line.split(',')]
                dictionary = dict(zip(colnames, data))
                dictlist.append(dictionary)
                print(dictionary)
    return dictlist
parse_file(DATAFILE)

# simplified version using csv module
def parse_csv(datafile):
    data = []
    with open(datafile, 'rb') as sd:
        r = csv.DictReader(sd)
        for line in r:
            data.append(line)
    return data
parse_csv(DATAFILE)