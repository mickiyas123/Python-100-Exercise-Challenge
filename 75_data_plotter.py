import pandas as pd
import pylab as plt

data = pd.read_csv("http://www.pythononhow.com/data/sampledata.txt")
data.plot(X='x' , Y="y" , kind ='scatter')
plt.show()


