import pandas as pd
from data_pipeline import extract, transform

def test_extract():
    df = extract()
    assert not df.empty, "提取的数据不应为空"
    assert set(df.columns) == {"id", "value"}, "应包含id和value列"

def test_transform():
    raw_data = pd.DataFrame({"id": [1], "value": ["TEST"]})
    processed = transform(raw_data)
    assert "processed" in processed.columns, "应添加processed列"
    assert processed.loc[0, "processed"] == "test", "value列应转为小写"
    