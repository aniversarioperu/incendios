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
f, ax = plt.subplots()

sns.barplot(x, y, ax=ax)
ax.set_xlabel('Fecha')
ax.set_ylabel('Número de tuits por día')
ax.set_title('Reportes de incendio desde la cuenta @bomberos')


plt.tight_layout()
plt.savefig('timeline' + sys.argv[1].strip() + '.svg', frameon=None)




sys.exit()
