# -*- coding: utf-8 -*-
import datetime
import sys

import prettyplotlib as ppl
from prettyplotlib import brewer2mpl
from pandas import DataFrame
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

import utils


path = 'RobotoCondensed.ttf'
prop = fm.FontProperties(fname=path)

filenames = [
    'tuits_incendio_2013.csv',
    'tuits_incendio_2014.csv',
]

filename = filenames[0]

# dates 2013 will show as 2014 so we can plot the two series together
dates_2013, y_2013 = utils.get_xy_values(filenames[0])
dates_2014, y_2014 = utils.get_xy_values(filenames[1])

# need to make sure y_2013 and y_2014 have same number of data points
# pad with zero
padding = [0]*(len(y_2014) - len(y_2013))
y_2013 = padding + y_2013

y_2013 = np.array(y_2013)
y_2014 = np.array(y_2014)

x_2013 = np.array(range(0, len(dates_2013), 1))
x_2014 = np.array(range(0, len(dates_2014), 1))

x_labels = []
for i in set(dates_2013 + dates_2014):
    if i.date() not in x_labels:
        x_labels.append(i.date())
x_labels.sort()

ind = np.arange(len(y_2014))
fig, ax = plt.subplots(1)
#rects1 = ax.bar(ind, y, width=0.5, color="#2ecc71", edgecolor="#3498db")
ax.set_xticks(ind)
ax.set_title('Reportes de incendio desde la cuenta @bomberos',
             size=22,
             fontproperties=prop,
             )
ax.tick_params(axis="x", color="gray", labelsize=8)

ax.set_xticklabels(x_labels)
plt.ylim([0, 60])
plt.xticks(rotation="90")

# queremos color
set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors
color = set2[0]

ax.set_xlabel('Fecha',
              size=14,
              fontproperties=prop,
              )
ax.set_ylabel('Número de tuits por día',
              size=14,
              fontproperties=prop,
              )

plt.plot(x_2014, y_2013, '#7f8c8d', x_2014, y_2014, '#27ae60')
plt.tight_layout()
plt.savefig('timeline_incendio_2013_vs_2014.svg', frameon=None)

if datetime.datetime(2014, 12, 25) in dates_2014:
    print("::PLOT IS READY TO PUBLISH::")
