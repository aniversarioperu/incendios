# -*- coding: utf-8 -*-
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


dates, y = utils.get_xy_values()
y = np.array(y)
print(y, len(y))
x = np.array(range(0, len(dates), 1))
print(x, len(dates))

x_labels = []
for i in dates:
    x_labels.append(i.date())

ind = np.arange(len(y))
fig, ax = plt.subplots(1)
#rects1 = ax.bar(ind, y, width=0.5, color="#2ecc71", edgecolor="#3498db")
ax.set_xticks(ind + 0.2)
ax.set_title('Reportes de incendio desde la cuenta @bomberos',
             size=22,
             fontproperties=prop,
             )
ax.tick_params(axis="x", color="gray", labelsize=8)

ax.set_xticklabels(x_labels)
plt.ylim([0,max(y) + 2])
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

plt.plot(x, y, color=color)
plt.tight_layout()
plt.savefig('timeline' + sys.argv[1].strip().replace(".csv", "") + '.svg', frameon=None)




