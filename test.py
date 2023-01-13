import numpy as np
import matplotlib.pyplot

x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)

matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.show()

print('i am here')