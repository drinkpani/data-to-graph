#!/usr/bin/python3

import matplotlib.pyplot as plt
import sys
import pandas as pd
df = pd.read_csv(f"data/{sys.argv[1]}.tsv", sep="\t")

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, sharex=True, figsize=(36,48), constrained_layout=True)
# fig.subplots_adjust(bottom=0.15)
fig.suptitle('August 2019\n', fontsize=60)

ax1.plot(df['LOCATION'], df['TURBIDITY (NTU)'], marker='.', color='r')
ax1.set_title('Turbidity', fontsize=40)
ax1.tick_params(labelrotation=90, labelsize=30)

ax2.plot(df['LOCATION'], df['PH VALUE'], marker='.', color='b')
ax2.set_title('Ph Value', fontsize=40)
ax2.tick_params(labelrotation=90, labelsize=30)


ax3.plot(df['LOCATION'], df['EC VALUE'], marker='.', color='g')
ax3.set_title('Electrical Conductivity', fontsize=40)
ax3.tick_params(labelrotation=90, labelsize=30)

ax4.plot(df['LOCATION'], df['ECOLI NO'],  marker='.', color='c')
ax4.set_title('Ecoli Count', fontsize=40)
ax4.tick_params(labelrotation=90, labelsize=30)

ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()

fig.savefig(f'exports/{sys.argv[1]}.png', facecolor=fig.get_facecolor(), edgecolor=None)