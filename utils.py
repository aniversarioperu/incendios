from itertools import groupby
import codecs
import sys
import re
import datetime
import time

def get_xy_values():
    f = codecs.open(sys.argv[1].strip(), "r", "utf-8")
    datos = f.readlines()
    f.close()

    x = []
    y = []
    for line in datos:
        line = line.strip()
        if re.search("^[0-9]{6,},", line) and 'incendio' in line.lower():
            line = line.split(",")
            fecha = line[1]
            fecha = fecha.split(" ")[0]
            date_object = datetime.datetime.strptime(fecha, "%Y-%m-%d")
            dia = datetime.datetime.strftime(date_object, '%d %b')

            y.append(dia)
            if dia not in x:
                x.append(dia)
    y = [len(list(group)) for key, group in groupby(y)]
    return x, y