from pipelines.transform import transform_data
import pandas as pd

def test_transform_data():
    test_data = pd.DataFrame({
        'order_date': ['2023-01-01', '2023-01-02'],
        'quantity': [2, 3],
        'unit_price': [10.0, 15.0]
    })

    transformed = transform_data(test_data)
    
    assert 'total_price' in transformed.columns
    assert transformed['total_price'].equals(pd.Series([20.0, 45.0]))
    assert pd.api.types.is_datetime64_dtype(transformed['order_date'])