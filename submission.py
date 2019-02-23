import numpy as np
import pandas as pd
import random

def submit(test_label, df_test, file="submission.csv"):
    test_sales_price = [np.exp(x) for x in test_label]
    print("Fist 10 predictions:", test_sales_price[:10])

    test_id = df_test.index
    data = {'Id': test_id,
    'SalePrice': test_sales_price
           }

    frame = pd.DataFrame(data)
    path = f'submissions/{file}'
    print("\nSave path :", path)
    frame.to_csv(path, index = False)
