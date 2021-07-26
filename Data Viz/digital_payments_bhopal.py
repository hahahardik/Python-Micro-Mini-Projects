import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = "data/D50-DigitalPayments_Bhopal_2017-18_2.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get