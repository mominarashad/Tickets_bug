def extract_context(row) -> dict:
    return {
        "issue": row["Summary"],
        "description": row["Detailed Description"],
        "root_cause": row["Root Cause"],
        "fix": row["Data Fix Provided"],
        "full_text": row["full_text"]
    }
