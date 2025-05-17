import pytest
from pipelines.extract import extract_csv
import os

def test_extract_csv_success():
    test_file = "data/raw/sales_data.csv"
    df = extract_csv(test_file)
    assert df is not None
    assert not df.empty

def test_extract_csv_fail():
    df = extract_csv("nonexistent_file.csv")
    assert df is None