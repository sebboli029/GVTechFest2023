import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y, color='red', label='sensor1')
plt.title('mi primer diagrama', fontdict={'fontname':'Comic Sans MS', 'fontsize':20})
plt.xlabel('time (seg)')
plt.ylabel('measure')
plt.legend()
plt.show()

