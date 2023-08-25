import numpy as np
import pandas as pd
import tensorflow as tf

with open('Minerva.npy', 'rb') as file:
    output = np.load(file, allow_pickle=True)

print(output)

# for label, feature in output:
#     print("Txt: ", label)
#     print("Hash: ", feature)

