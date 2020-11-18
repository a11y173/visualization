#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Author  :   Solanin
@License :   (C) Copyright 2013-2019
@Software:   PyCharm
@File    :   graph.py
@Time    :   2020/11/18 下午2:21
'''

import matplotlib.pyplot as plt
import pandas as pd


class graph:
    def Histogram(self,x,y,width,color,xlabel,ylabel,title,is_data_label):
        fig,ax = plt.subplots(figsize=(22,10),dpi=60)

        plt.bar(x=x,height=y,width=width,color=color)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)

        if is_data_label == 'Y':
            for x,y in zip(x,y):
                plt.text(x,y,y,ha='center',fontsize=10)
        else:
            pass

        plt.show()

if __name__ == "__main__":
    graph = graph()
    top_pop = pd.read_csv('top_country_pop.csv',encoding='utf8')
    x = top_pop['Country Name']
    y = top_pop['pops']

    graph.Histogram(x=x,
                    y=y,
                    width=0.8,
                    color='c',
                    xlabel='Country Name',
                    ylabel='Populations',
                    title='Top 15 Country Populations',
                    is_data_label='Y'
                    )



