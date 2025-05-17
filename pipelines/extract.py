import pandas as pd
from typing import Optional

def extract_csv(file_path: str) -> Optional[pd.DataFrame]:
    try:
        df = pd.read_csv(file_path)
        print(f"success extract data:{file_path}, line count: {len(df)}")
        return df
    except Exception as e:
        print(f"extract failed:{e}")
        return None