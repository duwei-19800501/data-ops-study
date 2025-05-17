import pandas as pd
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df['total_price'] = df['quantity'] * df['unit_price']
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df