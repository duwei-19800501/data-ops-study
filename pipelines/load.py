import pandas as pd
def load_to_csv(df: pd.DataFrame, output_path: str) -> bool:
    try:
        df.to_csv(output_path, index=False)
        print(f"数据已保存到: {output_path}")
        return True
    except Exception as e:
        print(f"保存失败: {e}")
        return False