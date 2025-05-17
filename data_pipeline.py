import pandas as pd

def extract():
    data = {'id':[1,2,3], 'value':['A','B','C']}
    return pd.DataFrame(data)

def transform(df):
    df['processed'] = df['value'].str.lower()
    return df

def load(df):
    df.to_csv('output_data.csv', index=False)
    print("Data loaded successfully")

raw_data = extract()
processed_data = transform(raw_data)
load(processed_data)