import codecs
import sys
import re
import datetime
import time

def get_x_values():
    timestamps = []
    counting = []
    f = codecs.open(sys.argv[1].strip(), "r", "utf-8")
    datos = f.readlines()
    f.close()
    x = []
    for line in datos:
        line = line.strip()
        if re.search("^[0-9]{6,},", line) and 'incendio' in line.lower():
            line = line.split(",")
            fecha = line[1]
            fecha = fecha.split(" ")[0]
            date_object = datetime.datetime.strptime(fecha, "%Y-%m-%d")
            mes = datetime.datetime.strftime(date_object, '%d %b')
            if date_object not in timestamps:
                timestamps.append(date_object)

            counting.append(fecha)
            print(mes)
            if mes not in x:
                x.append(mes)
    return x