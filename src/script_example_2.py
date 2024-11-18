# Code example 2

import pandas as pd

def manipulate_dataframe() -> None:
    """
    Creates a DataFrame from a dictionary and performs operations on it:
    - Prints the DataFrame.
    - Prints the 'Age' column.
    - Filters and prints the rows where 'Age' is greater than 30.
    """
    data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
    df = pd.DataFrame(data)
    print("DataFrame:\n", df)

    print("\nAges:\n", df["Age"])

    people_above_30 = df[df["Age"] > 30]
    print("\nPeople above 30 years old:\n", people_above_30)
