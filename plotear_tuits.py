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


x, y = utils.get_xy_values()
x = np.array(x)
y = np.array(y)

f, ax = plt.subplots(1)

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
ax.set_title('Reportes de incendio desde la cuenta @bomberos',
             size=22,
             fontproperties=prop,
             )


ax.set_xticklabels(x, rotation=90, 
              )

ppl.plot(ax, x, y, linewidth=3.0, color=color)

plt.tight_layout()
plt.savefig('timeline' + sys.argv[1].strip().replace(".csv", "") + '.svg', frameon=None)

sys.exit()
