import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


df=pd.read_csv('Topic_Survey_Assignment.csv',index_col=0)

df.sort_values(['Very interested'], ascending =False, axis=0, inplace=True)

color_list=['#5cb85c','#5bc0de','#d9534f']

ax = (df.div(df.sum(1), axis=0)).plot(kind='bar',
                                              figsize=(20,6),
                                              width = 0.8,
                                              rot=90,
                                              color = color_list,
                                              edgecolor=None)


for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy() 
    ax.annotate('{:.1%}'.format(height), (x, y + height + 0.01))
    
    
plt.title('Percentage of Respondents\' Interest in Data Science Areas',fontsize=16)
plt.legend(labels=df.columns, loc='upper right',fontsize=14) 


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.yticks([])
plt.tight_layout()

plt.show()
