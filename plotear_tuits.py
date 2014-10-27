# -*- coding: utf-8 -*-
import codecs
import datetime
from itertools import groupby
import json
import re
import time
import sys

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


path = 'RobotoCondensed.ttf'
prop = fm.FontProperties(fname=path)

plt.style.use('ggplot')

f = codecs.open(sys.argv[1].strip(), "r", "utf-8")
datos = f.readlines()
f.close()

timestamps = []
counting = []
x = []
for line in datos:
    line = line.strip()
    if re.search("^[0-9]{6,},", line) and 'incendio' in line.lower():
        line = line.split(",")
        fecha = line[1]
        unix_time = time.mktime(datetime.datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S +%f").timetuple())
        # correct for local time Lima -5 hours
        unix_time -= 60*60*5
        #print unix_time
        fecha = fecha.split(" ")[0]
        my_time = datetime.datetime.strptime(fecha, "%Y-%m-%d")
        if my_time not in timestamps:
            timestamps.append(my_time)

        counting.append(fecha)
        if fecha not in x:
            x.append(fecha)
        
# de reversa
timestamp = timestamps[::-1]
y_axis = [len(list(group)) for key, group in groupby(counting)]


fig, ax = plt.subplots(1)

plt.bar(timestamps, y_axis)
plt.yticks(size="14",
           fontproperties=prop,
           )
plt.xticks(rotation='45',
           size="14",
           fontproperties=prop,
           )
plt.ylabel('Número de tuits por día',
           size="16",
           fontproperties=prop,
           )
plt.title('Reportes de incendio desde la cuenta @bomberos',
          size="22",
          fontproperties=prop,
          )
plt.tight_layout()
plt.savefig('timeline' + sys.argv[1].strip() + '.svg', frameon=None)
sys.exit()
