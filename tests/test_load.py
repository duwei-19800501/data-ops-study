from pipelines.load import load_to_csv
from pipelines.transform import transform_data
import pandas as pd
import os

def test_load_to_csv(tmp_path):
    test_df = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
    output_file = tmp_path / "test_output.csv"
    
    assert load_to_csv(test_df, output_file)
    assert os.path.exists(output_file)