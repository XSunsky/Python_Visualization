# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:04:17 2019

@author: 56472
"""

import numpy as np
from matplotlib import pyplot as plt

def simplePloter():
    '''
    不适用包，简单绘制
    '''
    N=10
    theta=np.linspace(0.0,2*np.pi,N,endpoint=False)
    radii=10*np.random.rand(N)
    width=np.pi/4*np.random.rand(N)
    ax=plt.subplot(111, projection='polar')
    bars=ax.bar(theta,radii,width=width,bottom=0.0)
    for r, bar in zip(radii,bars):
        bar.set_facecolor(plt.cm.jet(r/10.))
        bar.set_alpha(0.8)
#    plt.savefig('simplePloter_windrose.png') 
    plt.show()

simplePloter()


#from windrose import WindroseAxes
#import numpy as np
#
#ws = np.random.random(10) * 2    # 值
#wd = np.random.random(5) * 180   # 方向
#
##ws = [1,2,3,4,5]
##wd = [10,20,30,70,90]
#
#ax = WindroseAxes.from_ax()
#ax.bar(wd, ws, normed=True, opening=0.8, edgecolor='white')
#ax.set_legend()