import hashlib
import csv
import numpy as np
import pandas as pd

with open('englishExam.txt', 'r') as file:
    with open('rawData.csv', 'w') as file2:
        fieldNames = ['Txt', 'Hash']
        writer = csv.DictWriter(file2, fieldnames=fieldNames)
        writer.writeheader()
        for line in file:
            line = line.strip()
            hasher = hashlib.sha256()
            hasher.update(line.encode('utf-8'))
            writer.writerow({'Txt': line, 'Hash': hasher.hexdigest()})

data = pd.read_csv('rawData.csv', sep=',', header=0)

print(data)

with open('Minerva.npy', 'wb') as file:
    np.save(file, data)
