import pandas as pd
from .data_fetch import get_monthly_batting_stats

def fix_double_escaped(x):
    try:
        # Decode the literal escape sequences first
        # Then decode as UTF-8 bytes
        return bytes(x, "utf-8").decode("unicode_escape").encode("latin1").decode("utf-8")
    except Exception:
        return x 
    
batting_df = get_monthly_batting_stats()


batting_df['Name'] = batting_df['Name'].apply(fix_double_escaped)
