import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

figure, ax = plt.subplots(2, 2)

df = pd.DataFrame(np.random.rand(10000, 2))

print(df)
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
ax[0][0].plot(numbers)
ax[0][1].plot([num * 2 for num in numbers])
ax[1][0].plot([num ** 2 for num in numbers])
ax[1][1].plot(df)

plt.show()
