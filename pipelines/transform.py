import pandas as pd
import great_expectations as gx
from typing import Optional

def validate_data(df: pd.DataFrame) -> bool:
    context = gx.get_context()
    result = context.run_checkpoint(
        checkpoint_name="sales_checkpoint",
        batch_request={
            "runtime_parameters": {"batch_data": df},
            "runtime_parameters": {"path": ""},
            "data_asset_name": "post_transform_data",
            "batch_identifiers": {"default_identifier": "default"}
        }
    )
    return result["success"]

def transform_data(df: pd.DataFrame) -> Optional[pd.DataFrame]:
    df = df.dropna()
    df['total_price'] = df['quantity'] * df['unit_price']
    df['order_date'] = pd.to_datetime(df['order_date'])
    
    if not validate_data(df):
        print("❌ 数据验证失败！详情见 gx/uncommitted/data_docs/")
        return None
    return df