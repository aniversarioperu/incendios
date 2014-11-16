# -*- coding: utf-8 -*-
import sys

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import utils


path = 'RobotoCondensed.ttf'
prop = fm.FontProperties(fname=path)

sns.set(style="whitegrid", font_scale=.9)

x, y = utils.get_xy_values()
x = np.array(x)
y = np.array(y)
f, ax = plt.subplots()

sns.pointplot(x, y, ax=ax, markers='.', color='#D0D0D0')
sns.despine(left=True)

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


ax.set_xticklabels(x, rotation=90)


plt.tight_layout()
plt.savefig('timeline' + sys.argv[1].strip().replace(".csv", "") + '.svg', frameon=None)

sys.exit()
