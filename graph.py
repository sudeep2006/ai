import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

data=pd.read_csv("C:/Users/SPTINT-11/Desktop/sudeep/tips.csv")
print(data)
plt.scatter(data['day'],data['tip'])
plt.xlabel('day')
plt.ylabel('tip')
plt.title('scatter plot')
plt.show()

plt.plot(data['day'])
plt.plot(data['size'])
plt.show()

plt.bar(data['day'],data['tip'])
plt.show()

plt.hist(data['total_bill'])
plt.show()
