# If not already installed, do: pip install pandas fastparquet
import pandas as pd

URL_DATA = 'https://storage.dosm.gov.my/population/population_malaysia.parquet'

df = pd.read_parquet(URL_DATA)
if 'date' in df.columns: df['date'] = pd.to_datetime(df['date'])

print(df)

# ImportError: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
# A suitable version of pyarrow or fastparquet is required for parquet support.
# Trying to import the above resulted in these errors:
#  - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
#  - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.