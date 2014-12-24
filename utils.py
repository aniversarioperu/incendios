from itertools import groupby
import codecs
import sys
import re
import datetime
import time


def remove_year_from_dates(dates):
    return [datetime.datetime.strftime(i, '%b %d') for i in dates]


def get_xy_values(filename):
    f = codecs.open(filename, "r", "utf-8")
    datos = f.readlines()
    f.close()

    x = []
    y = []
    nice_dates = []
    for line in datos:
        line = line.strip()
        if re.search("^[0-9]{6,},", line) and 'INCENDIO' in line:
            line = line.split(",")
            fecha = line[1]
            fecha_split = fecha.split(" ")
            fecha = fecha_split[0]
            if '2013' in fecha:
                fecha = fecha.replace('2013', '2014')
            fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d')
            #dia = datetime.datetime.strftime(date_object, '%d %b')

            y.append(fecha)
            if fecha not in x:
                x.append(fecha)
    y = [len(list(group)) for key, group in groupby(y)]
    return x[::-1], y[::-1]


def join_date_series(dates_2013, dates_2014):
    dates = dates_2013 + dates_2014
    dates_set = set(dates)
    dates_list = list(dates)
    print("list", len(dates_list), dates_list)
    return dates_list.sort()

