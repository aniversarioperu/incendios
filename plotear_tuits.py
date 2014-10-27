# -*- coding: utf-8 -*-
import codecs
import datetime
from itertools import groupby
import json
import re
import time
import sys

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import utils


sns.set(style="whitegrid")
rs = np.random.RandomState(7)

x, y = utils.get_xy_values()
x = np.array(x)
y = np.array(y)
print(">>> len(x)", len(x), x)
print(">>> len(y)", len(y))
f, ax = plt.subplots()

sns.barplot(x, y, ax=ax)
ax.set_ylabel("Sequential")


sns.despine(bottom=True)
plt.setp(f.axes, yticks=[])
plt.tight_layout(h_pad=3)
plt.savefig('timeline' + sys.argv[1].strip() + '.svg', frameon=None)




sys.exit()
path = 'RobotoCondensed.ttf'
prop = fm.FontProperties(fname=path)

plt.style.use('ggplot')


timestamps = []
counting = []

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
