import pandas as pd
from .data_fetch import get_monthly_batting_stats
from .constants import MLB_TEAM_NICKNAMES

TEAM_MAP = {
    "New York Maj-AL": "New York AL",
    "New York Maj-NL": "New York NL",
    "Los Angeles Maj-AL": "Los Angeles AL",
    "Los Angeles Maj-NL": "Los Angeles NL",
    "Chicago Maj-AL": "Chicago AL",
    "Chicago Maj-NL": "Chicago NL",
}

def fix_double_escaped(x):
    try:
        # Decode the literal escape sequences first
        # Then decode as UTF-8 bytes
        return bytes(x, "utf-8").decode("unicode_escape").encode("latin1").decode("utf-8")
    except Exception:
        return x 
        

batting_df = get_monthly_batting_stats()


batting_df['Name'] = batting_df['Name'].apply(fix_double_escaped)

# ---- disambiguate teams by league ----
# Extract "Maj-AL" or "Maj-NL" (handles cases where Lev might have other text)
league = batting_df["Lev"].str.extract(r"(Maj-(?:AL|NL))", expand=False)

# Build "City Maj-AL" / "City Maj-NL"
key = batting_df["Tm"].astype(str).str.strip() + " " + league.fillna("")

# Overwrite Tm where we have a mapping; otherwise keep original city
batting_df["Tm"] = key.map(TEAM_MAP).fillna(batting_df["Tm"].astype(str).str.strip())

# Change Team Names from Cities to Nicknames
batting_df['Tm'] = batting_df['Tm'].map(MLB_TEAM_NICKNAMES).fillna(batting_df['Tm'])
