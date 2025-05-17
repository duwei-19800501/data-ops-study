from pipelines.extract import extract_csv
from pipelines.transform import transform_data
from pipelines.load import load_to_csv

def main():
    input_path = "data/raw/sales_data.csv"
    output_path = "data/processed/cleaned_sales.csv"

    print("⏳ 开始ETL流程...")
    df = extract_csv(input_path)
    if df is not None:
        df_transformed = transform_data(df)
        if load_to_csv(df_transformed, output_path):
            print("✅ ETL 完成！输出文件:", output_path)
        else:
            print("❌ 数据加载失败")
    else:
        print("❌ 数据提取失败")

if __name__ == "__main__":
    main()