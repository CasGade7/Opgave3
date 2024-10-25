import pandas as pd

kildekode = "Opgave3/source_data.csv"
df = pd.read_csv(kildekode, skiprows=1, dtype={'customer_id': 'int64', 'name': 'string','email': 'string','purchase_amount':'float64'})
# Kunne ikke få det til at virke, da jeg aldrig fandt en løsning på at der var ,, i en af rækkerne.
# dette gjorde at der kommer en ekstra collum, fandt aldrig en løsning, så gik videre og ville komme tilbage,
# men nåede aldrig så langt
clean_df = df.dropna()

print(df)