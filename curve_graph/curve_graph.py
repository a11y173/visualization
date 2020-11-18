import matplotlib.pyplot as plt
import pandas as pd

top_15_pop = pd.read_csv('top_country_pop.csv',encoding='utf8')

fig,ax= plt.subplots(figsize=(22,10),dpi=60)


plt.bar(x=top_15_pop['Country Name'],
        height=top_15_pop['pops'],
        width=0.8,
        color = 'c'
        )




ax.set_xlabel('Country Name')
ax.set_ylabel('Poputions')
ax.set_title('Top 15 Country Poputions')

ax.set_xticklabels(top_15_pop['Country Name'], rotation = 45)

# 增加标签
for a,b in zip(top_15_pop['Country Name'],top_15_pop['pops']):
    plt.text(a,b,b,ha='center',fontsize=10)

plt.show()

