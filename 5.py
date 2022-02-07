import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Load in csv
pyber_ride_df = pd.read_csv("Resources/PyBer_ride_data.csv")
pyber_ride_df
pyber_ride_df.plot(x="Month", y="Avg. Fare ($USD)")
plt.show()
