import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('~/data/IL_schools_17/rc17.csv')

def diversity():
    diversityLabels = ['SCHOOL - WHITE %',
                       'SCHOOL - BLACK %',
                       'SCHOOL - HISPANIC %',
                       'SCHOOL - ASIAN %',
                       'SCHOOL - NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER %',
                       'SCHOOL - NATIVE AMERICAN %','SCHOOL - TWO OR MORE RACES %']
    
    diversityValues = [df[x].mean() for x in diversityLabels]

    plt.figure(figsize=(7, 8))
    ax = plt.subplot(111)  # create figure & 1 axis
    plt.title("Illinois Student Population Demographics")
    ax.axis("equal")
    pie = ax.pie(diversityValues)
    lgd = ax.legend([x[9:][:-1] for x in diversityLabels], bbox_to_anchor=(1.025, 0))
    plt.subplots_adjust(left=0.1, bottom=0.3, right=0.9)
    plt.figure(1).savefig('outfiles/il_rc17_racial_breakdown.png')

diversity()
