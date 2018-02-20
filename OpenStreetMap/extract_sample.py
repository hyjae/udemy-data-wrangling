import os

READFILE = 'south-korea-latest.osm'
WRITEFILE = 'example.osm'
SIZE = 1024 ** 2 * 30 # 30mb

string = '</node>'

def extract_sample(readfile, writefile, bytesize):
    statinfo = os.stat(readfile)

    with open(readfile, 'r') as r, open(writefile, 'w') as w:
        textsize = 0
        for i, line in enumerate(r):
            w.writelines(line)
            textsize += len(line.encode('utf-8'))
            if textsize > bytesize and line.find(string) != -1:
                break

        r.close()
        w.close()

    print("{} bytes out of {} bytes is copied into {}"
          .format(bytesize, statinfo.st_size, writefile))

if __name__ == '__main__':
    extract_sample(READFILE, WRITEFILE, SIZE)