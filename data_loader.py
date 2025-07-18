import pandas as pd

def load_and_prepare(file_path: str) -> pd.DataFrame:
    columns = ["Summary", "Detailed Description", "Root Cause", "Data Fix Provided"]
    df = pd.read_excel(file_path)

    # Drop rows with no Root Cause
    df = df[df["Root Cause"].notnull()].copy()
    df = df.reset_index(drop=True)

    # Replace NaN in selected columns
    df[columns] = df[columns].fillna("")

    # Create full context string
    df['full_text'] = df[columns].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
    return df
